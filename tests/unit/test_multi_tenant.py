"""Tests for the multi-tenant scaffold (PR 15)."""

from __future__ import annotations

import asyncio

import pytest

from src.multi_tenant import (
    MissingTenantError,
    TenantContext,
    get_tenant,
    require_tenant,
    sanitise_tenant_id,
    set_tenant,
    tenant_scoped_collection,
    tenant_scoped_graph,
    tenant_scoped_key,
    tenant_scoped_table,
    reset_tenant,
)


# ---------------------------------------------------------------------------
# Sanitisation
# ---------------------------------------------------------------------------


class TestSanitise:
    def test_pass_through_safe_id(self):
        assert sanitise_tenant_id("acme_corp_2026") == "acme_corp_2026"

    def test_non_alphanumeric_replaced(self):
        assert sanitise_tenant_id("acme-corp.io") == "acme_corp_io"
        assert sanitise_tenant_id("acme corp/eu") == "acme_corp_eu"

    def test_leading_digit_prefixed(self):
        assert sanitise_tenant_id("123corp") == "t123corp"

    def test_empty_returns_empty(self):
        assert sanitise_tenant_id("") == ""


# ---------------------------------------------------------------------------
# Context manager + getters
# ---------------------------------------------------------------------------


class TestTenantContext:
    def test_default_no_tenant(self):
        # Each test gets a fresh contextvar copy thanks to pytest's
        # per-test isolation -- but be defensive.
        assert get_tenant() is None

    def test_context_manager_sets_and_unsets(self):
        with TenantContext("acme"):
            assert get_tenant() == "acme"
        assert get_tenant() is None

    def test_nested_contexts_shadow(self):
        with TenantContext("outer"):
            assert get_tenant() == "outer"
            with TenantContext("inner"):
                assert get_tenant() == "inner"
            assert get_tenant() == "outer"
        assert get_tenant() is None

    def test_empty_tenant_id_raises(self):
        with pytest.raises(ValueError):
            TenantContext("")

    def test_imperative_set_reset(self):
        token = set_tenant("imp1")
        try:
            assert get_tenant() == "imp1"
        finally:
            reset_tenant(token)
        assert get_tenant() is None

    def test_context_manager_sanitises_id(self):
        with TenantContext("acme-corp.io"):
            assert get_tenant() == "acme_corp_io"

    def test_require_tenant_raises_when_unset(self):
        assert get_tenant() is None
        with pytest.raises(MissingTenantError):
            require_tenant()

    def test_require_tenant_returns_tenant(self):
        with TenantContext("acme"):
            assert require_tenant() == "acme"


# ---------------------------------------------------------------------------
# Async context manager
# ---------------------------------------------------------------------------


class TestAsyncTenantContext:
    @pytest.mark.asyncio
    async def test_async_context_manager(self):
        assert get_tenant() is None
        async with TenantContext("acme"):
            assert get_tenant() == "acme"
        assert get_tenant() is None

    @pytest.mark.asyncio
    async def test_tenant_isolated_across_tasks(self):
        # Each task should have its own copy of the contextvar.
        async def inner_task(tenant_id: str) -> str:
            async with TenantContext(tenant_id):
                await asyncio.sleep(0.01)
                return get_tenant() or ""

        results = await asyncio.gather(
            inner_task("a"), inner_task("b"), inner_task("c")
        )
        assert sorted(results) == ["a", "b", "c"]


# ---------------------------------------------------------------------------
# Naming helpers
# ---------------------------------------------------------------------------


class TestNamingHelpers:
    def test_table_unscoped_when_no_tenant(self):
        assert tenant_scoped_table("documents") == "documents"

    def test_table_scoped(self):
        with TenantContext("acme"):
            assert tenant_scoped_table("documents") == "documents_t_acme"

    def test_collection_unscoped_when_no_tenant(self):
        assert tenant_scoped_collection("ats") == "ats"

    def test_collection_scoped(self):
        with TenantContext("acme"):
            assert tenant_scoped_collection("ats") == "ats__t__acme"

    def test_key_unscoped_when_no_tenant(self):
        assert tenant_scoped_key("agent:1:sess") == "agent:1:sess"

    def test_key_scoped(self):
        with TenantContext("acme"):
            assert tenant_scoped_key("agent:1:sess") == "t:acme:agent:1:sess"

    def test_graph_unscoped_when_no_tenant(self):
        assert tenant_scoped_graph("cognee_graph") == "cognee_graph"

    def test_graph_scoped(self):
        with TenantContext("acme"):
            assert tenant_scoped_graph("cognee_graph") == "cognee_graph_t_acme"


# ---------------------------------------------------------------------------
# ENHANCED_REQUIRE_TENANT enforcement
# ---------------------------------------------------------------------------


class TestRequireTenantEnvVar:
    def test_raises_when_required_but_unset(self, monkeypatch):
        monkeypatch.setenv("ENHANCED_REQUIRE_TENANT", "1")
        with pytest.raises(MissingTenantError):
            tenant_scoped_table("documents")
        with pytest.raises(MissingTenantError):
            tenant_scoped_collection("ats")
        with pytest.raises(MissingTenantError):
            tenant_scoped_key("k")
        with pytest.raises(MissingTenantError):
            tenant_scoped_graph("g")

    def test_passes_when_tenant_set(self, monkeypatch):
        monkeypatch.setenv("ENHANCED_REQUIRE_TENANT", "1")
        with TenantContext("acme"):
            assert tenant_scoped_table("documents") == "documents_t_acme"

    def test_off_by_default(self, monkeypatch):
        monkeypatch.delenv("ENHANCED_REQUIRE_TENANT", raising=False)
        # No exception even without a tenant set
        assert tenant_scoped_table("documents") == "documents"
