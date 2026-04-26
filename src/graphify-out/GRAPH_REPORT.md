# Graph Report - .  (2026-04-26)

## Corpus Check
- 76 files · ~112,944 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2802 nodes · 7595 edges · 43 communities detected
- Extraction: 51% EXTRACTED · 49% INFERRED · 0% AMBIGUOUS · INFERRED: 3742 edges (avg confidence: 0.59)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Multi-Tenant Management|Multi-Tenant Management]]
- [[_COMMUNITY_Memory Data Models|Memory Data Models]]
- [[_COMMUNITY_Agent Memory Integration|Agent Memory Integration]]
- [[_COMMUNITY_Security Framework|Security Framework]]
- [[_COMMUNITY_Backup Manager|Backup Manager]]
- [[_COMMUNITY_Document Processor and AI|Document Processor and AI]]
- [[_COMMUNITY_Anthropic LLM Client|Anthropic LLM Client]]
- [[_COMMUNITY_Advanced Analytics Engine|Advanced Analytics Engine]]
- [[_COMMUNITY_MCP Memory Tools|MCP Memory Tools]]
- [[_COMMUNITY_API Key Management|API Key Management]]
- [[_COMMUNITY_Memory CRUD Operations|Memory CRUD Operations]]
- [[_COMMUNITY_Enhanced MCP Server Config|Enhanced MCP Server Config]]
- [[_COMMUNITY_Undo Manager|Undo Manager]]
- [[_COMMUNITY_Approval Workflow|Approval Workflow]]
- [[_COMMUNITY_WebSocket Realtime Server|WebSocket Realtime Server]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]
- [[_COMMUNITY_Community 19|Community 19]]
- [[_COMMUNITY_Community 20|Community 20]]
- [[_COMMUNITY_Community 21|Community 21]]
- [[_COMMUNITY_Community 22|Community 22]]
- [[_COMMUNITY_Community 23|Community 23]]
- [[_COMMUNITY_Community 24|Community 24]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]
- [[_COMMUNITY_Community 40|Community 40]]
- [[_COMMUNITY_Community 41|Community 41]]
- [[_COMMUNITY_Community 42|Community 42]]

## God Nodes (most connected - your core abstractions)
1. `AgentMemoryIntegration` - 375 edges
2. `SMCMemoryWrapper` - 199 edges
3. `SubAgentCoordinator` - 150 edges
4. `AgentMessage` - 142 edges
5. `TaskPriority` - 141 edges
6. `AgentTask` - 141 edges
7. `MessageType` - 133 edges
8. `ATSMemoryWrapper` - 130 edges
9. `OMAMemoryWrapper` - 113 edges
10. `AgentStatus` - 113 edges

## Surprising Connections (you probably didn't know these)
- `Central registry for managing all 21 agents across categories` --uses--> `AgentMemoryIntegration`  [INFERRED]
  agents\__init__.py → agent_memory_integration.py
- `Initialize all critical agents` --uses--> `AgentMemoryIntegration`  [INFERRED]
  agents\__init__.py → agent_memory_integration.py
- `Create a specific agent by ID` --uses--> `AgentMemoryIntegration`  [INFERRED]
  agents\__init__.py → agent_memory_integration.py
- `Get an existing agent instance` --uses--> `AgentMemoryIntegration`  [INFERRED]
  agents\__init__.py → agent_memory_integration.py
- `Create all agents in a specific category` --uses--> `AgentMemoryIntegration`  [INFERRED]
  agents\__init__.py → agent_memory_integration.py

## Hyperedges (group relationships)
- **** — deduplication_template, intent_detection_template, summarization_template [INFERRED 0.85]
- **** — extraction_template, quality_check_template, deduplication_template [INFERRED 0.82]
- **** — json_output_format, confidence_score_pattern, placeholder_pattern [EXTRACTED 0.95]

## Communities

### Community 0 - "Multi-Tenant Management"
Cohesion: 0.01
Nodes (256): Create database schema for tenant isolation, Initialize tenant-specific configuration, AdvancedSearchEngine, Advanced Search with Re-ranking for Enhanced Cognee Implements semantic search, Expand query with synonyms and related terms          Args:             query, Re-ranking strategies, Use LLM to generate related search queries, Extract keywords and generate variant queries (+248 more)

### Community 1 - "Memory Data Models"
Cohesion: 0.02
Nodes (181): MemoryEntry, MemorySearchResult, MemoryType, Types of memory entries (common across all projects), AlgorithmicTradingSystem, create_algorithmic_trading_system(), example_usage(), Execute a trade based on signal or manual request (+173 more)

### Community 2 - "Agent Memory Integration"
Cohesion: 0.05
Nodes (184): AgentMemoryIntegration, BaseModel, Update context for a session or agent, Context Manager Agent     SMC agent responsible for managing shared context acr, Retrieve context for a session or agent, Share context between agents, Create a snapshot of current context state, Restore context from a snapshot (+176 more)

### Community 3 - "Security Framework"
Cohesion: 0.02
Nodes (137): BaseHTTPMiddleware, DependencyUpdater, EnhancedInputValidator, EnhancedPasswordPolicy, EnhancedRateLimiter, EnhancedSecurityFramework, FileScanner, rate_limit() (+129 more)

### Community 4 - "Backup Manager"
Cohesion: 0.02
Nodes (117): BackupManager, Enhanced Cognee - Backup Manager  Comprehensive backup system for Enhanced Cog, Create a backup of specified databases.          Args:             backup_typ, Backup a specific database.          Args:             database: Database nam, Backup PostgreSQL using pg_dump., Backup Qdrant using snapshot API., Backup Neo4j using backup API., Backup Redis using RDB snapshot. (+109 more)

### Community 5 - "Document Processor and AI"
Cohesion: 0.02
Nodes (117): DocumentProcessor, DocumentProcessorManager, main(), Enhanced Cognee - Document Auto-Processor  Automatically processes documents w, Stop watching for file changes., Handle file creation events.          Args:             event: FileCreatedEve, Determine if file should be auto-processed.          Args:             file_p, Check if file is a document type we process. (+109 more)

### Community 6 - "Anthropic LLM Client"
Cohesion: 0.03
Nodes (88): ABC, AnthropicClient, Enhanced Cognee - Anthropic Claude LLM Provider  Implementation of Anthropic C, Make a basic Claude API call.          Args:             prompt: The prompt t, Internal method to call Claude API.          Args:             prompt: User p, Make a Claude API call with message history.          Args:             messa, Internal method to call Claude API with messages.          Args:, Make a Claude API call expecting JSON response.          Args:             pr (+80 more)

### Community 7 - "Advanced Analytics Engine"
Cohesion: 0.03
Nodes (74): AdvancedAnalyticsEngine, analytics_engine(), AnalyticsDashboard, AnalyticsEvent, AnalyticsMetric, IsolationLevel, main(), multi_tenant_manager() (+66 more)

### Community 8 - "MCP Memory Tools"
Cohesion: 0.03
Nodes (75): Exception, Enhanced Cognee - Standard Memory MCP Tools Module  This module contains the s, Delete a specific memory (Standard Memory MCP Tool)      TRIGGER TYPE: (M) Man, Add a memory entry (Standard Memory MCP Tool)      This is the standard memory, List all agents that have stored memories (Standard Memory MCP Tool)      TRIG, AuthorizationError, Authorizer, BackupCreationError (+67 more)

### Community 9 - "API Key Management"
Cohesion: 0.03
Nodes (53): APIKey, APIKeyManager, ecosystem_manager(), EcosystemManager, Integration, IntegrationManager, IntegrationType, Issue (+45 more)

### Community 10 - "Memory CRUD Operations"
Cohesion: 0.05
Nodes (47): main(), Close all connections, Example usage of the Agent Memory Integration with DYNAMIC configuration      Th, # NOTE: Agent must be registered in .enhanced-cognee-config.json, DEPRECATED: Agent registry is now loaded from configuration          This method, Initialize connections to Enhanced stack components, Initialize Qdrant collections for each configured category, Add memory entry for specific agent with Enhanced stack integration          Par (+39 more)

### Community 11 - "Enhanced MCP Server Config"
Cohesion: 0.05
Nodes (27): EnhancedConfig, KnowledgeRelation, lifespan(), MemoryEntry, Get list of active agents from PostgreSQL, Manage application lifecycle, Load dynamic category prefixes from configuration file, SearchQuery (+19 more)

### Community 12 - "Undo Manager"
Cohesion: 0.04
Nodes (40): from_dict(), get_undo_manager(), init_undo_manager(), Enhanced Cognee - Undo Manager for Automated Actions  This module provides a c, Manages undo operations for Enhanced Cognee automations.      Features:     -, Initialize the undo manager.          Args:             config_path: Path to, Load automation configuration., Get default configuration. (+32 more)

### Community 13 - "Approval Workflow"
Cohesion: 0.06
Nodes (30): ApprovalRequest, ApprovalWorkflowManager, CLIApprovalWorkflow, DashboardApprovalWorkflow, main(), Enhanced Cognee - Approval Workflow System  Provides approval workflow for aut, Approve an approval request.          Args:             request_id: Request I, Reject an approval request.          Args:             request_id: Request ID (+22 more)

### Community 14 - "WebSocket Realtime Server"
Cohesion: 0.07
Nodes (25): EventType, Handle new WebSocket client connection, Handle incoming message from client, WebSocket event types, Clean up disconnected client, Send event to specific client, Broadcast event to all subscribed clients, Subscribe client to event type (+17 more)

### Community 15 - "Community 15"
Cohesion: 0.05
Nodes (28): APIKeyManager, JWTAuthenticator, main(), Permission, Enhanced Cognee - Authentication & Authorization System  Implements JWT authen, Create a JWT token.          Args:             user_id: User identifier, Verify and decode a JWT token.          Args:             token: JWT token st, Refresh an expired token.          Args:             token: Original token (+20 more)

### Community 16 - "Community 16"
Cohesion: 0.08
Nodes (20): MaintenanceScheduler, MockMCPClient, Enhanced Cognee - Maintenance Scheduler  Automated maintenance system for Enha, Add event listeners for job execution., Start the maintenance scheduler., Stop the maintenance scheduler., Schedule all configured maintenance tasks., Schedule a single maintenance task. (+12 more)

### Community 17 - "Community 17"
Cohesion: 0.07
Nodes (21): detect_language(), detect_language_metadata(), LanguageDetector, Language Detection Module for Enhanced Cognee  Supports 28 languages with auto, Check if language is supported, Get language name from code.          Args:             language_code: ISO la, Get all supported languages, Detect language and return full metadata.          Args:             text: Te (+13 more)

### Community 18 - "Community 18"
Cohesion: 0.06
Nodes (22): EncryptionManager, GDPRCompliance, main(), PIIDetector, Enhanced Cognee - Encryption & Data Protection  Implements encryption at rest,, Decrypt a dictionary.          Args:             ciphertext: Encrypted dictio, Personally Identifiable Information (PII) detector.      Detects and masks PII, Initialize PII detector. (+14 more)

### Community 19 - "Community 19"
Cohesion: 0.07
Nodes (18): AuditLogger, Initialize the audit logger.          Args:             config_path: Path to, Load automation configuration., Get default configuration., Setup file-based logger., Check if operation should be logged based on config., Anonymize sensitive data in log entries., Log an automated operation.          Args:             operation_type: Type o (+10 more)

### Community 20 - "Community 20"
Cohesion: 0.08
Nodes (19): AutoConfiguration, main(), Enhanced Cognee - Auto-Configuration System  Automatically configures Enhanced, Detect available ports for Enhanced stack., Check if port is available., Detect LLM provider from environment variables., Determine recommended installation mode., Generate secure passwords. (+11 more)

### Community 21 - "Community 21"
Cohesion: 0.07
Nodes (20): ContextInjector, main(), Enhanced Cognee - Session Manager  Manages Claude Code sessions for multi-prom, Get session information.          Args:             session_id: Session ID, Get full context from a session.          Args:             session_id: Sessi, Get recent sessions for a user/agent.          Args:             user_id: Use, Manager for Claude Code sessions.      Handles session lifecycle, context inje, Get the most recent active session for a user/agent.          Args: (+12 more)

### Community 22 - "Community 22"
Cohesion: 0.09
Nodes (19): AgentRegistry, create_agent(), create_critical_agents(), example_usage(), get_agent_system_info(), Get an existing agent instance, Create all agents in a specific category, Get information about an agent (+11 more)

### Community 23 - "Community 23"
Cohesion: 0.09
Nodes (14): AdvancedSearch, Advanced Search Module for Enhanced Cognee  Provides faceted search, autocompl, Perform fuzzy search with typo tolerance.          Args:             query: S, Advanced search features with faceting and suggestions, Get facet value counts for filtering UI.          Args:             memories:, Extract language from memory metadata, Extract memory type from metadata, Extract category from metadata (+6 more)

### Community 24 - "Community 24"
Cohesion: 0.08
Nodes (16): AutoCategorizer, Auto-categorize a memory.          Args:             content: Memory content, Detect memory type from content., Detect memory concept from content., Extract file paths from content.          Args:             content: Memory c, Extract facts from content.          Args:             content: Memory conten, Structured memory model manager.      Handles hierarchical observations with t, Initialize structured memory model.          Args:             db_pool: Postg (+8 more)

### Community 25 - "Community 25"
Cohesion: 0.11
Nodes (28): Confidence Score Pattern (0.0-1.0 scale across all templates), Deduplication Analysis Factors (semantic, structural, entity overlap, contextual), Exact Duplicate Detection (score 0.95-1.0), Merge Strategies (keep_one, keep_most_complete, merge, keep_both, keep_newer, keep_older, chronological), Near Duplicate Detection (score 0.85-0.95), Deduplication Prompt Template, Entity Extraction Confidence Scoring (0.95-1.0 explicit, 0.85-0.95 strong, 0.70-0.85 reasonable, 0.50-0.70 low), Entity Categories (10 types: people, orgs, systems, files, technologies, concepts, dates, numbers, locations, events) (+20 more)

### Community 26 - "Community 26"
Cohesion: 0.18
Nodes (5): ContextManager, create_context_manager(), example_usage(), create_smc_agent(), Factory function to create SMC agents

### Community 27 - "Community 27"
Cohesion: 0.12
Nodes (8): PerformanceAnalytics, PerformanceMetrics, Performance Analytics Module for Enhanced Cognee Collects and exposes performanc, Export metrics in Prometheus text format          Returns:             Prometheu, Get slow queries above threshold, Performance metrics data structure, Collects and manages performance metrics, Record a query execution time

### Community 28 - "Community 28"
Cohesion: 0.12
Nodes (15): authorization_error_response(), confirmation_required_response(), error_response(), format_response(), format_response_compact(), Enhanced Cognee - MCP Response Formatter  Standardizes all MCP tool return val, Create a confirmation required response.      Args:         operation: Operat, Format a response dictionary as JSON string.      Args:         response: Res (+7 more)

### Community 29 - "Community 29"
Cohesion: 0.15
Nodes (7): PerformanceOptimizer, Performance Optimization Module for Enhanced Cognee  Optimizes database querie, Track query performance metrics, Get performance statistics, Performance optimization for multi-language queries, Benchmark query performance.          Args:             postgres_pool: Postgr, Optimized search query with language filtering.          Args:             qu

### Community 30 - "Community 30"
Cohesion: 0.5
Nodes (3): main(), Enhanced Cognee - Progressive Disclosure Search  Implements 3-layer progressiv, Test progressive disclosure search.

### Community 31 - "Community 31"
Cohesion: 0.5
Nodes (3): Real-Time Memory Synchronization Module for Enhanced Cognee Enables real-time me, Represents a synchronization event, SyncEvent

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (1): Multi-Agent System (MAS) specific categories         This is ONE EXAMPLE of how

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (1): Generic default categories for simple projects         Projects can override wi

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (1): Create from dictionary.

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (1): Context manager for database cursor.          Yields:             SQLite curs

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (1): Make a basic LLM API call.          Args:             prompt: The prompt to s

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (1): Make an LLM API call with message history.          Args:             message

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (1): Make an LLM API call expecting JSON response.          Args:             prom

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (1): Get current available tokens.

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (1): Get seconds until tokens available.

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (1): Related But Not Duplicate (score 0.50-0.85)

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (1): Distinct Memory (score 0.0-0.50)

## Knowledge Gaps
- **832 isolated node(s):** `Advanced Search Module for Enhanced Cognee  Provides faceted search, autocompl`, `Advanced search features with faceting and suggestions`, `Perform faceted search with multiple filters.          Args:             memo`, `Get autocomplete suggestions for search query.          Args:             par`, `Perform fuzzy search with typo tolerance.          Args:             query: S` (+827 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 32`** (1 nodes): `Multi-Agent System (MAS) specific categories         This is ONE EXAMPLE of how`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (1 nodes): `Generic default categories for simple projects         Projects can override wi`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (1 nodes): `Create from dictionary.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (1 nodes): `Context manager for database cursor.          Yields:             SQLite curs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (1 nodes): `Make a basic LLM API call.          Args:             prompt: The prompt to s`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (1 nodes): `Make an LLM API call with message history.          Args:             message`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (1 nodes): `Make an LLM API call expecting JSON response.          Args:             prom`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (1 nodes): `Get current available tokens.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (1 nodes): `Get seconds until tokens available.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (1 nodes): `Related But Not Duplicate (score 0.50-0.85)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (1 nodes): `Distinct Memory (score 0.0-0.50)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `AgentMemoryIntegration` connect `Agent Memory Integration` to `Multi-Tenant Management`, `Memory Data Models`, `Anthropic LLM Client`, `Memory CRUD Operations`, `Enhanced MCP Server Config`, `Community 22`, `Community 26`?**
  _High betweenness centrality (0.130) - this node is a cross-community bridge._
- **Why does `SQLiteManager` connect `Backup Manager` to `Multi-Tenant Management`, `Memory Data Models`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Are the 355 inferred relationships involving `AgentMemoryIntegration` (e.g. with `MemoryConfigManager` and `MemoryCategoryConfig`) actually correct?**
  _`AgentMemoryIntegration` has 355 INFERRED edges - model-reasoned connections that need verification._
- **Are the 220 inferred relationships involving `str` (e.g. with `.get_search_analytics()` and `.add_memory()`) actually correct?**
  _`str` has 220 INFERRED edges - model-reasoned connections that need verification._
- **Are the 178 inferred relationships involving `SMCMemoryWrapper` (e.g. with `ContextManager` and `Context Manager Agent     SMC agent responsible for managing shared context acr`) actually correct?**
  _`SMCMemoryWrapper` has 178 INFERRED edges - model-reasoned connections that need verification._
- **Are the 130 inferred relationships involving `SubAgentCoordinator` (e.g. with `TaskRequest` and `WorkflowRequest`) actually correct?**
  _`SubAgentCoordinator` has 130 INFERRED edges - model-reasoned connections that need verification._
- **Are the 137 inferred relationships involving `AgentMessage` (e.g. with `ContextManager` and `Context Manager Agent     SMC agent responsible for managing shared context acr`) actually correct?**
  _`AgentMessage` has 137 INFERRED edges - model-reasoned connections that need verification._