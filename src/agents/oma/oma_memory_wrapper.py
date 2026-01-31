#!/usr/bin/env python3
"""
OMA (Other Multi-Agent) Memory Wrapper
Specialized memory interface for development and analysis agents
Integrates with Enhanced Cognee stack
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, timedelta
from ...agent_memory_integration import (
    AgentMemoryIntegration, MemoryCategory, MemoryType, MemoryEntry,
    MemorySearchResult
)

logger = logging.getLogger(__name__)

class OMAMemoryWrapper:
    """Specialized memory wrapper for OMA category agents"""

    def __init__(self, integration: AgentMemoryIntegration):
        self.integration = integration
        self.oma_agents = [
            "code-reviewer",
            "code-analyzer",
            "bug-detector",
            "test-generator",
            "documentation-writer",
            "security-auditor",
            "performance-analyzer",
            "log-analyzer",
            "dependency-manager",
            "ci-cd-orchestrator"
        ]

    async def store_code_review(self, agent_id: str, review_data: Dict[str, Any],
                                metadata: Dict[str, Any] = None) -> str:
        """Store code review results"""
        content = self._format_code_review(review_data)

        enhanced_metadata = {
            **(metadata or {}),
            "review_type": review_data.get("review_type"),
            "file_path": review_data.get("file_path"),
            "language": review_data.get("language"),
            "framework": review_data.get("framework"),
            "reviewer": review_data.get("reviewer"),
            "quality_score": review_data.get("quality_score"),
            "issue_count": len(review_data.get("issues", []))
        }

        return await self.integration.add_memory(
            agent_id=agent_id,
            content=content,
            memory_type=MemoryType.PROCEDURAL,
            metadata=enhanced_metadata,
            tags=["code_review", "quality", "analysis"]
        )

    async def store_code_analysis(self, agent_id: str, analysis: Dict[str, Any],
                                   metadata: Dict[str, Any] = None) -> str:
        """Store code analysis results"""
        content = self._format_code_analysis(analysis)

        enhanced_metadata = {
            **(metadata or {}),
            "analysis_type": analysis.get("analysis_type"),
            "file_path": analysis.get("file_path"),
            "metrics": analysis.get("metrics", {}),
            "complexity_score": analysis.get("complexity_score"),
            "suggestions_count": len(analysis.get("suggestions", [])),
            "dependencies": analysis.get("dependencies", [])
        }

        return await self.integration.add_memory(
            agent_id=agent_id,
            content=content,
            memory_type=MemoryType.FACTUAL,
            metadata=enhanced_metadata,
            tags=["code_analysis", "metrics", "suggestions"]
        )

    async def store_bug_report(self, agent_id: str, bug_data: Dict[str, Any],
                                severity: str = "medium", metadata: Dict[str, Any] = None) -> str:
        """Store bug detection report"""
        content = self._format_bug_report(bug_data)

        enhanced_metadata = {
            **(metadata or {}),
            "bug_type": bug_data.get("bug_type"),
            "file_path": bug_data.get("file_path"),
            "line_number": bug_data.get("line_number"),
            "severity": severity,
            "priority": bug_data.get("priority", "normal"),
            "auto_detected": bug_data.get("auto_detected", True),
            "false_positive": bug_data.get("false_positive", False)
        }

        return await self.integration.add_memory(
            agent_id=agent_id,
            content=content,
            memory_type=MemoryType.EPISODIC,
            metadata=enhanced_metadata,
            tags=["bug", "issue", "detection"]
        )

    async def store_test_case(self, agent_id: str, test_case: Dict[str, Any],
                              metadata: Dict[str, Any] = None) -> str:
        """Store generated test case"""
        content = self._format_test_case(test_case)

        enhanced_metadata = {
            **(metadata or {}),
            "test_type": test_case.get("test_type"),
            "test_file": test_case.get("test_file"),
            "test_function": test_case.get("test_function"),
            "assertions": test_case.get("assertions", []),
            "coverage": test_case.get("coverage"),
            "framework": test_case.get("framework")
        }

        return await self.integration.add_memory(
            agent_id=agent_id,
            content=content,
            memory_type=MemoryType.PROCEDURAL,
            metadata=enhanced_metadata,
            tags=["test_case", "automation", "quality"]
        )

    async def store_documentation(self, agent_id: str, doc_data: Dict[str, Any],
                                 metadata: Dict[str, Any] = None) -> str:
        """Store generated or updated documentation"""
        content = self._format_documentation(doc_data)

        enhanced_metadata = {
            **(metadata or {}),
            "doc_type": doc_data.get("doc_type"),
            "file_path": doc_data.get("file_path"),
            "format": doc_data.get("format"),
            "language": doc_data.get("language"),
            "sections": doc_data.get("sections", []),
            "auto_generated": doc_data.get("auto_generated", True)
        }

        return await self.integration.add_memory(
            agent_id=agent_id,
            content=content,
            memory_type=MemoryType.SEMANTIC,
            metadata=enhanced_metadata,
            tags=["documentation", "knowledge", "sharing"]
        )

    async def store_security_scan(self, agent_id: str, security_data: Dict[str, Any],
                                    risk_level: str = "medium", metadata: Dict[str, Any] = None) -> str:
        """Store security audit results"""
        content = self._format_security_scan(security_data)

        enhanced_metadata = {
            **(metadata or {}),
            "scan_type": security_data.get("scan_type"),
            "file_path": security_data.get("file_path"),
            "vulnerability_type": security_data.get("vulnerability_type"),
            "risk_level": risk_level,
            "cvss_score": security_data.get("cvss_score"),
            "recommendations": security_data.get("recommendations", [])
        }

        return await self.integration.add_memory(
            agent_id=agent_id,
            content=content,
            memory_type=MemoryType.FACTUAL,
            metadata=enhanced_metadata,
            tags=["security", "audit", "vulnerability"]
        )

    async def search_code_issues(self, agent_id: str = None, file_path: str = None,
                                 language: str = None, severity: str = None,
                                 limit: int = 50) -> List[MemorySearchResult]:
        """Search for code-related issues"""
        query_parts = []
        if file_path:
            query_parts.append(file_path)
        if language:
            query_parts.append(language)
        if severity:
            query_parts.append(severity)

        query = " ".join(query_parts) if query_parts else None

        return await self.integration.search_memory(
            agent_id=agent_id,
            query=query,
            category=MemoryCategory.OMA,
            limit=limit
        )

    async def search_bugs(self, agent_id: str = None, bug_type: str = None,
                           severity: str = None, fixed: bool = None,
                           limit: int = 50) -> List[MemorySearchResult]:
        """Search for bug reports"""
        query_parts = ["bug"]
        if bug_type:
            query_parts.append(bug_type)
        if severity:
            query_parts.append(severity)
        if fixed is not None:
            query_parts.append("fixed" if fixed else "unfixed")

        query = " ".join(query_parts)

        return await self.integration.search_memory(
            agent_id=agent_id,
            query=query,
            memory_type=MemoryType.EPISODIC,
            category=MemoryCategory.OMA,
            limit=limit
        )

    async def get_code_quality_metrics(self, agent_id: str, days_back: int = 30) -> Dict[str, Any]:
        """Get code quality metrics for OMA agent"""
        try:
            # Get recent code-related memories
            reviews = await self.search_code_issues(agent_id, limit=1000)
            analyses = await self.integration.search_memory(
                agent_id=agent_id,
                query="analysis metrics",
                category=MemoryCategory.OMA,
                limit=500
            )

            # Analyze quality metrics
            quality_score = 0
            issues_fixed = 0
            issues_open = 0
            coverage_avg = 0

            # Analyze reviews
            for review in reviews:
                if "quality_score" in review.metadata:
                    quality_score += review.metadata["quality_score"]
                if "issue_count" in review.metadata:
                    issues_open += review.metadata["issue_count"]

            # Analyze analyses
            coverage_values = []
            for analysis in analyses:
                if "coverage" in analysis.metadata and analysis.metadata["coverage"]:
                    coverage_values.append(analysis.metadata["coverage"])

            if coverage_values:
                coverage_avg = sum(coverage_values) / len(coverage_values)

            return {
                "agent_id": agent_id,
                "period_days": days_back,
                "code_quality": {
                    "average_quality_score": quality_score / len(reviews) if reviews else 0,
                    "total_reviews": len(reviews),
                    "total_analyses": len(analyses),
                    "average_coverage": coverage_avg,
                    "open_issues": issues_open,
                    "fixed_issues": issues_fixed
                }
            }
        except Exception as e:
            logger.error(f"Failed to get code quality metrics for {agent_id}: {e}")
            return {"error": str(e)}

    async def get_dependency_insights(self, project_path: str = None) -> Dict[str, Any]:
        """Get dependency management insights across OMA agents"""
        insights = {
            "project_path": project_path,
            "analysis": {},
            "recommendations": []
        }

        for agent_id in self.oma_agents:
            try:
                # Search for dependency-related memories
                dep_memories = await self.integration.search_memory(
                    agent_id=agent_id,
                    query="dependencies",
                    category=MemoryCategory.OMA,
                    limit=100
                )

                # Analyze dependency patterns
                dependencies = set()
                vulnerabilities = []
                outdated_deps = []

                for memory in dep_memories:
                    if "dependencies" in memory.metadata:
                        for dep in memory.metadata["dependencies"]:
                            dependencies.add(dep)
                    if "vulnerability" in memory.tags:
                        vulnerabilities.append({
                            "package": memory.metadata.get("package", "Unknown"),
                            "severity": memory.metadata.get("severity", "Medium")
                        })

                insights["analysis"][agent_id] = {
                    "total_dependencies": len(dependencies),
                    "dependencies_list": list(dependencies),
                    "vulnerabilities_found": len(vulnerabilities),
                    "recent_analysis": max([m.created_at for m in dep_memories],
                                            default=None).isoformat() if dep_memories else None
                }

            except Exception as e:
                logger.error(f"Failed to analyze dependencies for {agent_id}: {e}")
                insights["analysis"][agent_id] = {"error": str(e)}

        # Generate recommendations
        all_dependencies = set()
        for agent_data in insights["analysis"].values():
            if "dependencies_list" in agent_data:
                all_dependencies.update(agent_data["dependencies_list"])

        insights["recommendations"] = self._generate_dependency_recommendations(all_dependencies)

        return insights

    async def get_ci_cd_insights(self, agent_id: str = None, status: str = None,
                                hours_back: int = 24) -> Dict[str, Any]:
        """Get CI/CD pipeline insights"""
        insights = {
            "time_period": f"{hours_back} hours",
            "analysis": {}
        }

        agents_to_check = [agent_id] if agent_id else self.oma_agents

        for agent in agents_to_check:
            if agent not in self.oma_agents:
                continue

            try:
                # Search for CI/CD related memories
                ci_memories = await self.integration.search_memory(
                    agent_id=agent,
                    query="pipeline build deploy ci cd",
                    category=MemoryCategory.OMA,
                    limit=200
                )

                # Analyze pipeline performance
                builds_total = 0
                builds_success = 0
                builds_failed = 0
                deploy_count = 0

                for memory in ci_memories:
                    if "pipeline" in memory.tags:
                        builds_total += 1
                        if "success" in memory.tags:
                            builds_success += 1
                        elif "failed" in memory.tags:
                            builds_failed += 1
                    elif "deploy" in memory.tags:
                        deploy_count += 1

                insights["analysis"][agent] = {
                    "builds_total": builds_total,
                    "builds_success": builds_success,
                    "builds_failed": builds_failed,
                    "deploy_count": deploy_count,
                    "success_rate": (builds_success / builds_total * 100) if builds_total > 0 else 0,
                    "recent_activity": len(ci_memories)
                }

            except Exception as e:
                logger.error(f"Failed to analyze CI/CD for {agent}: {e}")
                insights["analysis"][agent] = {"error": str(e)}

        return insights

    def _format_code_review(self, review_data: Dict[str, Any]) -> str:
        """Format code review for storage"""
        return f"Code review for {review_data.get('file_path', 'Unknown file')}:\n" \
               f"Quality score: {review_data.get('quality_score', 'N/A')}\n" \
               f"Issues found: {len(review_data.get('issues', []))}\n" \
               f"Review type: {review_data.get('review_type', 'General review')}\n" \
               f"Key points: {'; '.join(review_data.get('key_points', []))}\n" \
               f"Recommendations: {'; '.join(review_data.get('recommendations', []))}"

    def _format_code_analysis(self, analysis: Dict[str, Any]) -> str:
        """Format code analysis for storage"""
        return f"Code analysis for {analysis.get('file_path', 'Unknown file')}:\n" \
               f"Complexity score: {analysis.get('complexity_score', 'N/A')}\n" \
               f"Analysis type: {analysis.get('analysis_type', 'General analysis')}\n" \
               f"Key metrics: {analysis.get('metrics', {})}\n" \
               f"Suggestions: {len(analysis.get('suggestions', []))} suggestions provided\n" \
               f"Dependencies: {len(analysis.get('dependencies', []))} dependencies identified"

    def _format_bug_report(self, bug_data: Dict[str, Any]) -> str:
        """Format bug report for storage"""
        return f"Bug detected in {bug_data.get('file_path', 'Unknown file')}:\n" \
               f"Line {bug_data.get('line_number', 'Unknown')}: {bug_data.get('description', 'No description')}\n" \
               f"Bug type: {bug_data.get('bug_type', 'Unknown')}\n" \
               f"Auto-detected: {bug_data.get('auto_detected', False)}\n" \
               f"Severity: {bug_data.get('severity', 'Medium')}\n" \
               f"Recommended fix: {bug_data.get('suggested_fix', 'No fix suggested')}"

    def _format_test_case(self, test_case: Dict[str, Any]) -> str:
        """Format test case for storage"""
        return f"Test case generated for {test_case.get('test_file', 'Unknown')}:\n" \
               f"Function: {test_case.get('test_function', 'Unknown')}\n" \
               f"Test type: {test_case.get('test_type', 'Unknown')}\n" \
               f"Assertions: {len(test_case.get('assertions', []))}\n" \
               f"Expected behavior: {test_case.get('expected', 'Not specified')}\n" \
               f"Framework: {test_case.get('framework', 'Unknown')}"

    def _format_documentation(self, doc_data: Dict[str, Any]) -> str:
        """Format documentation for storage"""
        return f"Documentation generated for {doc_data.get('file_path', 'Unknown')}:\n" \
               f"Type: {doc_data.get('doc_type', 'Unknown')}\n" \
               f"Format: {doc_data.get('format', 'Unknown')}\n" \
               f"Sections: {', '.join(doc_data.get('sections', []))}\n" \
               f"Auto-generated: {doc_data.get('auto_generated', False)}\n" \
               f"Summary: {doc_data.get('summary', 'No summary provided')}"

    def _format_security_scan(self, security_data: Dict[str, Any]) -> str:
        """Format security scan for storage"""
        return f"Security scan completed for {security_data.get('file_path', 'Unknown')}:\n" \
               f"Scan type: {security_data.get('scan_type', 'Unknown')}\n" \
               f"Vulnerability: {security_data.get('vulnerability_type', 'Unknown')}\n" \
               f"Risk level: {security_data.get('risk_level', 'Medium')}\n" \
               f"CVSS Score: {security_data.get('cvss_score', 'Not calculated')}\n" \
               f"Recommendations: {len(security_data.get('recommendations', []))} recommendations provided"

    def _generate_dependency_recommendations(self, dependencies: set) -> List[str]:
        """Generate dependency management recommendations"""
        recommendations = []

        if len(dependencies) > 100:
            recommendations.append("Consider reducing dependency count to improve maintainability")

        if any("express" in dep.lower() for dep in dependencies):
            recommendations.append("Review Express.js dependencies for security updates")

        if any("package-lock.json" not in str(dep) for dep in dependencies):
            recommendations.append("Implement dependency locking for reproducible builds")

        if any(dep.startswith("0.") for dep in dependencies):
            recommendations.append("Review pre-release dependencies for production use")

        return recommendations

# Usage example
async def example_usage():
    """Example usage of OMA Memory Wrapper"""
    # Initialize integration
    integration = AgentMemoryIntegration()
    await integration.initialize()

    # Create OMA wrapper
    oma_wrapper = OMAMemoryWrapper(integration)

    # Example: Store code review
    review_data = {
        "file_path": "src/trading_engine/order_processor.py",
        "review_type": "Security Review",
        "quality_score": 8.5,
        "issues": [
            {"type": "security", "description": "SQL injection vulnerability", "line": 45},
            {"type": "performance", "description": "Inefficient loop", "line": 78}
        ],
        "key_points": ["Overall good structure", "Security concerns addressed"],
        "recommendations": ["Fix SQL injection", "Optimize loops"]
    }

    memory_id = await oma_wrapper.store_code_review(
        agent_id="code-reviewer",
        review_data=review_data,
        metadata={"framework": "Django", "language": "python"}
    )

    print(f"Stored code review with ID: {memory_id}")

    # Search for code issues
    issues = await oma_wrapper.search_code_issues(
        agent_id="code-reviewer",
        language="python",
        severity="high"
    )

    print(f"Found {len(issues)} high-severity code issues")

    # Get quality metrics
    metrics = await oma_wrapper.get_code_quality_metrics("code-analyzer")
    print(f"Code quality metrics: {metrics}")

    await integration.close()

if __name__ == "__main__":
    asyncio.run(example_usage())