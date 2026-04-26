# Graph Report - .  (2026-04-26)

## Corpus Check
- Corpus is ~34,080 words - fits in a single context window. You may not need a graph.

## Summary
- 279 nodes · 221 edges · 84 communities detected
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 19 edges (avg confidence: 0.81)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Dashboard REST API|Dashboard REST API]]
- [[_COMMUNITY_Docker Deployment Stack|Docker Deployment Stack]]
- [[_COMMUNITY_Realtime Hooks and Memory Detail|Realtime Hooks and Memory Detail]]
- [[_COMMUNITY_Next.js Dashboard Frontend|Next.js Dashboard Frontend]]
- [[_COMMUNITY_Memory List Page|Memory List Page]]
- [[_COMMUNITY_Edit Memory Modal|Edit Memory Modal]]
- [[_COMMUNITY_API Realtime Route|API Realtime Route]]
- [[_COMMUNITY_Add Memory Modal|Add Memory Modal]]
- [[_COMMUNITY_Error Boundary Component|Error Boundary Component]]
- [[_COMMUNITY_Form Validation and Design Patterns|Form Validation and Design Patterns]]
- [[_COMMUNITY_Bar Chart Component|Bar Chart Component]]
- [[_COMMUNITY_Line Chart Component|Line Chart Component]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
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
- [[_COMMUNITY_Community 43|Community 43]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]
- [[_COMMUNITY_Community 62|Community 62]]
- [[_COMMUNITY_Community 63|Community 63]]
- [[_COMMUNITY_Community 64|Community 64]]
- [[_COMMUNITY_Community 65|Community 65]]
- [[_COMMUNITY_Community 66|Community 66]]
- [[_COMMUNITY_Community 67|Community 67]]
- [[_COMMUNITY_Community 68|Community 68]]
- [[_COMMUNITY_Community 69|Community 69]]
- [[_COMMUNITY_Community 70|Community 70]]
- [[_COMMUNITY_Community 71|Community 71]]
- [[_COMMUNITY_Community 72|Community 72]]
- [[_COMMUNITY_Community 73|Community 73]]
- [[_COMMUNITY_Community 74|Community 74]]
- [[_COMMUNITY_Community 75|Community 75]]
- [[_COMMUNITY_Community 76|Community 76]]
- [[_COMMUNITY_Community 77|Community 77]]
- [[_COMMUNITY_Community 78|Community 78]]
- [[_COMMUNITY_Community 79|Community 79]]
- [[_COMMUNITY_Community 80|Community 80]]
- [[_COMMUNITY_Community 81|Community 81]]
- [[_COMMUNITY_Community 82|Community 82]]
- [[_COMMUNITY_Community 83|Community 83]]

## God Nodes (most connected - your core abstractions)
1. `Next.js 14 App Router Dashboard` - 11 edges
2. `FastAPI Backend` - 9 edges
3. `FastAPI Backend Container (Port 8000)` - 6 edges
4. `MemoryResponse` - 4 edges
5. `update_memory()` - 4 edges
6. `useToast()` - 4 edges
7. `SystemStatsResponse` - 3 edges
8. `SearchResponse` - 3 edges
9. `get_system_stats()` - 3 edges
10. `useRealTimeUpdates()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `Next.js 14 App Router Dashboard` --implements--> `WCAG 2.1 AA Accessibility Audit`  [INFERRED]
  nextjs-dashboard/README.md → PHASE_4_COMPLETION_REPORT.md
- `Next.js 14 App Router Dashboard` --references--> `SVG Logo - Next.js Wordmark (black text)`  [INFERRED]
  nextjs-dashboard/README.md → nextjs-dashboard/public/next.svg
- `Next.js 14 App Router Dashboard` --references--> `SVG Logo - Vercel Triangle (white)`  [INFERRED]
  nextjs-dashboard/README.md → nextjs-dashboard/public/vercel.svg
- `update_memory()` --calls--> `GET()`  [INFERRED]
  dashboard_api.py → app\api\realtime\route.ts
- `useRealTimeUpdates()` --calls--> `useToast()`  [INFERRED]
  hooks\use-realtime-updates.ts → nextjs-dashboard\src\hooks\use-toast.ts

## Hyperedges (group relationships)
- **Full-stack dashboard application: Phase 1 frontend foundation + Phase 4 polish + FastAPI backend serving Enhanced Cognee memory system data** — PHASE_4_COMPLETION_REPORT_phase4, PHASE_1_phase1_foundation, NJS_README_nextjs14_dashboard, README_fastapi_backend, shared_enhanced_cognee_memory [EXTRACTED 0.92]
- **Docker Compose stack provides isolated containerized deployment of all Enhanced Cognee memory databases for the dashboard** — DOCKER_stack, DOCKER_fastapi_container, DOCKER_postgres_container, DOCKER_qdrant_container, DOCKER_neo4j_container, DOCKER_redis_container [EXTRACTED 0.95]
- **Real-time update pipeline: SSE streams backend events to frontend, triggering toast notifications on CRUD operations** — PHASE_4_COMPLETION_REPORT_sse_integration, PHASE_4_COMPLETION_REPORT_toast_system, PHASE_4_COMPLETION_REPORT_backend_crud_api [EXTRACTED 0.90]

## Communities

### Community 0 - "Dashboard REST API"
Cohesion: 0.03
Nodes (62): BaseModel, add_memory(), dashboard_root(), delete_memory(), get_activity_data(), get_current_user(), get_db_pool(), get_graph_data() (+54 more)

### Community 1 - "Docker Deployment Stack"
Cohesion: 0.1
Nodes (23): FastAPI Backend Container (Port 8000), Neo4j Container (Port 27687), Next.js Dashboard Container (Port 3000), Nginx Reverse Proxy (Port 80), PostgreSQL Container (Port 25432), Qdrant Container (Port 26333), Redis Container (Port 26379), API Client with Axios Interceptors (+15 more)

### Community 2 - "Realtime Hooks and Memory Detail"
Cohesion: 0.23
Nodes (9): MemoryDetailPage(), useMemoryRealTimeUpdates(), useRealTimeUpdates(), addToRemoveQueue(), dispatch(), genId(), reducer(), toast() (+1 more)

### Community 3 - "Next.js Dashboard Frontend"
Cohesion: 0.18
Nodes (12): Lucide React Icons, Next.js 14 App Router Dashboard, Radix UI Accessible Primitives, Recharts Data Visualization, Vitest Testing Framework, Phase 1 Foundation Implementation, Tailwind CSS 4.x Integration, WCAG 2.1 AA Accessibility Audit (+4 more)

### Community 4 - "Memory List Page"
Cohesion: 0.25
Nodes (0): 

### Community 5 - "Edit Memory Modal"
Cohesion: 0.32
Nodes (3): handleBackdropClick(), handleClose(), handleKeyDown()

### Community 6 - "API Realtime Route"
Cohesion: 0.33
Nodes (3): Update an existing memory., update_memory(), GET()

### Community 7 - "Add Memory Modal"
Cohesion: 0.4
Nodes (0): 

### Community 8 - "Error Boundary Component"
Cohesion: 0.4
Nodes (0): 

### Community 9 - "Form Validation and Design Patterns"
Cohesion: 0.5
Nodes (5): React Hook Form + Zod Validation, Atomic Design Pattern (Atoms, Molecules, Organisms), AddMemoryModal Component, EditMemoryModal Component, Error Boundaries (React and Next.js)

### Community 10 - "Bar Chart Component"
Cohesion: 0.5
Nodes (0): 

### Community 11 - "Line Chart Component"
Cohesion: 0.5
Nodes (0): 

### Community 12 - "Community 12"
Cohesion: 0.5
Nodes (0): 

### Community 13 - "Community 13"
Cohesion: 0.5
Nodes (0): 

### Community 14 - "Community 14"
Cohesion: 0.5
Nodes (4): TanStack Query (React Query v5) Setup, ConnectionStatus Component, SSE Integration (useSSE Hook), SSE Streaming for Real-Time Updates

### Community 15 - "Community 15"
Cohesion: 0.5
Nodes (4): Enhanced Loading States (PageLoader, Skeletons), Performance Optimization (Code Splitting, Memoization), API Pagination, prometheus-client - Metrics Collection

### Community 16 - "Community 16"
Cohesion: 0.5
Nodes (4): Enhanced Cognee Logo (Blue #3b82f6, Brain/Neural Network), Icon Generation Guide (PWA Icons), Production Polish (PWA Manifest, SEO), robots.txt - Search Engine Crawl Configuration

### Community 17 - "Community 17"
Cohesion: 0.67
Nodes (0): 

### Community 18 - "Community 18"
Cohesion: 0.67
Nodes (0): 

### Community 19 - "Community 19"
Cohesion: 0.67
Nodes (0): 

### Community 20 - "Community 20"
Cohesion: 0.67
Nodes (3): JWT Authentication, passlib - Password Hashing (bcrypt), PyJWT - JWT Token Library

### Community 21 - "Community 21"
Cohesion: 1.0
Nodes (0): 

### Community 22 - "Community 22"
Cohesion: 1.0
Nodes (0): 

### Community 23 - "Community 23"
Cohesion: 1.0
Nodes (0): 

### Community 24 - "Community 24"
Cohesion: 1.0
Nodes (0): 

### Community 25 - "Community 25"
Cohesion: 1.0
Nodes (0): 

### Community 26 - "Community 26"
Cohesion: 1.0
Nodes (0): 

### Community 27 - "Community 27"
Cohesion: 1.0
Nodes (0): 

### Community 28 - "Community 28"
Cohesion: 1.0
Nodes (0): 

### Community 29 - "Community 29"
Cohesion: 1.0
Nodes (0): 

### Community 30 - "Community 30"
Cohesion: 1.0
Nodes (0): 

### Community 31 - "Community 31"
Cohesion: 1.0
Nodes (0): 

### Community 32 - "Community 32"
Cohesion: 1.0
Nodes (0): 

### Community 33 - "Community 33"
Cohesion: 1.0
Nodes (0): 

### Community 34 - "Community 34"
Cohesion: 1.0
Nodes (0): 

### Community 35 - "Community 35"
Cohesion: 1.0
Nodes (0): 

### Community 36 - "Community 36"
Cohesion: 1.0
Nodes (0): 

### Community 37 - "Community 37"
Cohesion: 1.0
Nodes (0): 

### Community 38 - "Community 38"
Cohesion: 1.0
Nodes (0): 

### Community 39 - "Community 39"
Cohesion: 1.0
Nodes (0): 

### Community 40 - "Community 40"
Cohesion: 1.0
Nodes (0): 

### Community 41 - "Community 41"
Cohesion: 1.0
Nodes (0): 

### Community 42 - "Community 42"
Cohesion: 1.0
Nodes (0): 

### Community 43 - "Community 43"
Cohesion: 1.0
Nodes (0): 

### Community 44 - "Community 44"
Cohesion: 1.0
Nodes (0): 

### Community 45 - "Community 45"
Cohesion: 1.0
Nodes (2): Enhanced Cognee Dashboard (Backend API + Frontend POC), Enhanced Cognee Memory System

### Community 46 - "Community 46"
Cohesion: 1.0
Nodes (2): SVG Icon - File Document (16x16, grayscale), SVG Icon - Application Window (16x16, grayscale)

### Community 47 - "Community 47"
Cohesion: 1.0
Nodes (0): 

### Community 48 - "Community 48"
Cohesion: 1.0
Nodes (0): 

### Community 49 - "Community 49"
Cohesion: 1.0
Nodes (0): 

### Community 50 - "Community 50"
Cohesion: 1.0
Nodes (0): 

### Community 51 - "Community 51"
Cohesion: 1.0
Nodes (0): 

### Community 52 - "Community 52"
Cohesion: 1.0
Nodes (0): 

### Community 53 - "Community 53"
Cohesion: 1.0
Nodes (0): 

### Community 54 - "Community 54"
Cohesion: 1.0
Nodes (0): 

### Community 55 - "Community 55"
Cohesion: 1.0
Nodes (0): 

### Community 56 - "Community 56"
Cohesion: 1.0
Nodes (0): 

### Community 57 - "Community 57"
Cohesion: 1.0
Nodes (0): 

### Community 58 - "Community 58"
Cohesion: 1.0
Nodes (0): 

### Community 59 - "Community 59"
Cohesion: 1.0
Nodes (0): 

### Community 60 - "Community 60"
Cohesion: 1.0
Nodes (0): 

### Community 61 - "Community 61"
Cohesion: 1.0
Nodes (0): 

### Community 62 - "Community 62"
Cohesion: 1.0
Nodes (0): 

### Community 63 - "Community 63"
Cohesion: 1.0
Nodes (0): 

### Community 64 - "Community 64"
Cohesion: 1.0
Nodes (0): 

### Community 65 - "Community 65"
Cohesion: 1.0
Nodes (0): 

### Community 66 - "Community 66"
Cohesion: 1.0
Nodes (0): 

### Community 67 - "Community 67"
Cohesion: 1.0
Nodes (0): 

### Community 68 - "Community 68"
Cohesion: 1.0
Nodes (0): 

### Community 69 - "Community 69"
Cohesion: 1.0
Nodes (0): 

### Community 70 - "Community 70"
Cohesion: 1.0
Nodes (0): 

### Community 71 - "Community 71"
Cohesion: 1.0
Nodes (0): 

### Community 72 - "Community 72"
Cohesion: 1.0
Nodes (0): 

### Community 73 - "Community 73"
Cohesion: 1.0
Nodes (0): 

### Community 74 - "Community 74"
Cohesion: 1.0
Nodes (0): 

### Community 75 - "Community 75"
Cohesion: 1.0
Nodes (0): 

### Community 76 - "Community 76"
Cohesion: 1.0
Nodes (0): 

### Community 77 - "Community 77"
Cohesion: 1.0
Nodes (0): 

### Community 78 - "Community 78"
Cohesion: 1.0
Nodes (0): 

### Community 79 - "Community 79"
Cohesion: 1.0
Nodes (1): httpx - Async HTTP Client

### Community 80 - "Community 80"
Cohesion: 1.0
Nodes (1): Docker Compose Stack Architecture

### Community 81 - "Community 81"
Cohesion: 1.0
Nodes (1): Zustand Client State Management

### Community 82 - "Community 82"
Cohesion: 1.0
Nodes (1): TypeScript Strict Mode

### Community 83 - "Community 83"
Cohesion: 1.0
Nodes (1): SVG Icon - Globe/World (16x16, grayscale)

## Knowledge Gaps
- **73 isolated node(s):** `Enhanced Cognee - Dashboard REST API  FastAPI-based REST API for web dashboard`, `Dependency injection for database pool.`, `Health check endpoint.`, `Get system statistics.`, `List memories with pagination and filtering.` (+68 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 21`** (2 nodes): `RootLayout()`, `layout.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 22`** (2 nodes): `not-found.tsx`, `NotFound()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 23`** (2 nodes): `page.tsx`, `Home()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 24`** (2 nodes): `providers.tsx`, `Providers()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 25`** (2 nodes): `page.tsx`, `AgentsPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 26`** (2 nodes): `page.tsx`, `handleDayClick()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 27`** (2 nodes): `page.tsx`, `DeveloperPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 28`** (2 nodes): `page.tsx`, `GraphPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 29`** (2 nodes): `page.tsx`, `handleMemoryClick()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 30`** (2 nodes): `page.tsx`, `SearchPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 31`** (2 nodes): `page.tsx`, `SettingsPage()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 32`** (2 nodes): `Badge()`, `Badge.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 33`** (2 nodes): `ConnectionStatus()`, `ConnectionStatus.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 34`** (2 nodes): `Skeleton.tsx`, `Skeleton()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 35`** (2 nodes): `Spinner.tsx`, `Spinner()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 36`** (2 nodes): `Header()`, `Header.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 37`** (2 nodes): `LoadingButton()`, `LoadingButton.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 38`** (2 nodes): `MemoryCard()`, `MemoryCard.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 39`** (2 nodes): `PieChart.tsx`, `CustomTooltip()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 40`** (2 nodes): `GraphNodeDetails()`, `GraphNodeDetails.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 41`** (2 nodes): `KnowledgeGraph()`, `KnowledgeGraph.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 42`** (2 nodes): `MemoryListSkeleton()`, `MemoryListSkeleton.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 43`** (2 nodes): `SearchInterface.tsx`, `handleResultClick()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 44`** (2 nodes): `Toaster.tsx`, `Toaster()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 45`** (2 nodes): `Enhanced Cognee Dashboard (Backend API + Frontend POC)`, `Enhanced Cognee Memory System`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 46`** (2 nodes): `SVG Icon - File Document (16x16, grayscale)`, `SVG Icon - Application Window (16x16, grayscale)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 47`** (1 nodes): `eslint.config.mjs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 48`** (1 nodes): `next-env.d.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 49`** (1 nodes): `next.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 50`** (1 nodes): `playwright.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 51`** (1 nodes): `postcss.config.mjs`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 52`** (1 nodes): `tailwind.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 53`** (1 nodes): `vitest.config.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 54`** (1 nodes): `vitest.setup.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 55`** (1 nodes): `error.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 56`** (1 nodes): `page.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 57`** (1 nodes): `page.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 58`** (1 nodes): `page.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 59`** (1 nodes): `Button.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 60`** (1 nodes): `Card.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 61`** (1 nodes): `Checkbox.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 62`** (1 nodes): `DropdownMenu.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 63`** (1 nodes): `index.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 64`** (1 nodes): `Input.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 65`** (1 nodes): `Textarea.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 66`** (1 nodes): `Button.test.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 67`** (1 nodes): `index.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 68`** (1 nodes): `Sidebar.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 69`** (1 nodes): `KPICard.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 70`** (1 nodes): `AnalyticsDashboard.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 71`** (1 nodes): `MemoryDetailSkeleton.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 72`** (1 nodes): `PageLoader.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 73`** (1 nodes): `SessionTimeline.tsx`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 74`** (1 nodes): `a11y-audit.spec.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 75`** (1 nodes): `analytics.spec.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 76`** (1 nodes): `graph.spec.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 77`** (1 nodes): `memories.spec.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 78`** (1 nodes): `timeline.spec.ts`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 79`** (1 nodes): `httpx - Async HTTP Client`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 80`** (1 nodes): `Docker Compose Stack Architecture`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 81`** (1 nodes): `Zustand Client State Management`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 82`** (1 nodes): `TypeScript Strict Mode`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 83`** (1 nodes): `SVG Icon - Globe/World (16x16, grayscale)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `FastAPI Backend` connect `Docker Deployment Stack` to `Next.js Dashboard Frontend`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._
- **Why does `update_memory()` connect `API Realtime Route` to `Dashboard REST API`?**
  _High betweenness centrality (0.009) - this node is a cross-community bridge._
- **Why does `Next.js 14 App Router Dashboard` connect `Next.js Dashboard Frontend` to `Docker Deployment Stack`?**
  _High betweenness centrality (0.008) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Next.js 14 App Router Dashboard` (e.g. with `Next.js Dashboard Container (Port 3000)` and `SVG Logo - Next.js Wordmark (black text)`) actually correct?**
  _`Next.js 14 App Router Dashboard` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Enhanced Cognee - Dashboard REST API  FastAPI-based REST API for web dashboard`, `Dependency injection for database pool.`, `Health check endpoint.` to the rest of the system?**
  _73 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Dashboard REST API` be split into smaller, more focused modules?**
  _Cohesion score 0.03 - nodes in this community are weakly interconnected._
- **Should `Docker Deployment Stack` be split into smaller, more focused modules?**
  _Cohesion score 0.1 - nodes in this community are weakly interconnected._