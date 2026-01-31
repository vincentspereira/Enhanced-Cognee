"""
Production Performance Optimization and Tuning Framework
Implements comprehensive performance optimization for production deployment
"""

import os
import json
import time
import asyncio
import logging
import subprocess
import statistics
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict, field
from enum import Enum
from datetime import datetime, timezone, timedelta
from contextlib import asynccontextmanager

import aiohttp
import psutil
import pytest
import yaml
from concurrent.futures import ThreadPoolExecutor

logger = logging.getLogger(__name__)


class OptimizationTarget(Enum):
    """Performance optimization targets"""
    THROUGHPUT = "throughput"
    LATENCY = "latency"
    CPU = "cpu"
    MEMORY = "memory"
    I_O = "i_o"
    NETWORK = "network"
    DATABASE = "database"
    CACHE = "cache"


class OptimizationStrategy(Enum):
    """Performance optimization strategies"""
    VERTICAL_SCALING = "vertical_scaling"
    HORIZONTAL_SCALING = "horizontal_scaling"
    CACHING = "caching"
    CONNECTION_POOLING = "connection_pooling"
    QUERY_OPTIMIZATION = "query_optimization"
    INDEX_OPTIMIZATION = "index_optimization"
    RESOURCE_TUNING = "resource_tuning"
    LOAD_BALANCING = "load_balancing"


@dataclass
class PerformanceBaseline:
    """Performance baseline metrics"""
    target: OptimizationTarget
    baseline_name: str
    metrics: Dict[str, float]
    timestamp: datetime
    environment: str = "production"
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OptimizationRecommendation:
    """Performance optimization recommendation"""
    recommendation_id: str
    target: OptimizationTarget
    strategy: OptimizationStrategy
    description: str
    expected_improvement: float
    implementation_complexity: str
    risk_level: str
    estimated_effort: str
    prerequisites: List[str] = field(default_factory=list)
    steps: List[str] = field(default_factory=list)
    rollback_plan: List[str] = field(default_factory=list)


@dataclass
class OptimizationResult:
    """Results of applied optimization"""
    optimization_id: str
    recommendation_id: str
    target: OptimizationTarget
    strategy: OptimizationStrategy
    before_metrics: Dict[str, float]
    after_metrics: Dict[str, float]
    improvement_percentage: float
    implementation_time: timedelta
    success: bool
    side_effects: List[str] = field(default_factory=list)
    next_steps: List[str] = field(default_factory=list)


@dataclass
class ResourceUtilization:
    """System resource utilization metrics"""
    cpu_percentage: float
    memory_percentage: float
    disk_usage_percentage: float
    network_io_bytes_sent: int
    network_io_bytes_recv: int
    disk_io_read_bytes: int
    disk_io_write_bytes: int
    active_connections: int
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class DatabasePerformanceMetrics:
    """Database performance metrics"""
    query_time_avg: float
    query_time_p95: float
    query_time_p99: float
    connections_active: int
    connections_idle: int
    cache_hit_ratio: float
    index_usage_ratio: float
    slow_queries_count: int
    deadlocks_count: int
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


@dataclass
class CachePerformanceMetrics:
    """Cache performance metrics"""
    hit_ratio: float
    miss_ratio: float
    eviction_count: int
    memory_usage_bytes: int
    operations_per_second: float
    average_response_time: float
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ResourceMonitor:
    """System resource monitoring"""

    def __init__(self):
        self.monitoring_interval = 1.0  # seconds
        self.resource_history: List[ResourceUtilization] = []
        self.max_history_size = 1000

    async def start_monitoring(self, duration_seconds: int = 60) -> List[ResourceUtilization]:
        """Start resource monitoring for specified duration"""
        logger.info(f"Starting resource monitoring for {duration_seconds} seconds")

        self.resource_history.clear()
        start_time = time.time()

        while time.time() - start_time < duration_seconds:
            utilization = await self._collect_resource_metrics()
            self.resource_history.append(utilization)

            # Limit history size
            if len(self.resource_history) > self.max_history_size:
                self.resource_history = self.resource_history[-self.max_history_size:]

            await asyncio.sleep(self.monitoring_interval)

        logger.info(f"Collected {len(self.resource_history)} resource samples")
        return self.resource_history

    async def _collect_resource_metrics(self) -> ResourceUtilization:
        """Collect current resource utilization metrics"""
        # CPU and memory
        cpu_percent = psutil.cpu_percent(interval=0.1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # Network I/O
        network = psutil.net_io_counters()

        # Disk I/O
        disk_io = psutil.disk_io_counters()

        # Network connections
        connections = len(psutil.net_connections())

        return ResourceUtilization(
            cpu_percentage=cpu_percent,
            memory_percentage=memory.percent,
            disk_usage_percentage=disk.percent,
            network_io_bytes_sent=network.bytes_sent,
            network_io_bytes_recv=network.bytes_recv,
            disk_io_read_bytes=disk_io.read_bytes,
            disk_io_write_bytes=disk_io.write_bytes,
            active_connections=connections
        )

    def get_resource_summary(self) -> Dict[str, Any]:
        """Get summary of resource utilization"""
        if not self.resource_history:
            return {}

        cpu_values = [r.cpu_percentage for r in self.resource_history]
        memory_values = [r.memory_percentage for r in self.resource_history]
        network_sent_values = [r.network_io_bytes_sent for r in self.resource_history]
        network_recv_values = [r.network_io_bytes_recv for r in self.resource_history]

        return {
            "cpu": {
                "avg": statistics.mean(cpu_values),
                "min": min(cpu_values),
                "max": max(cpu_values),
                "p95": self._percentile(cpu_values, 95)
            },
            "memory": {
                "avg": statistics.mean(memory_values),
                "min": min(memory_values),
                "max": max(memory_values),
                "p95": self._percentile(memory_values, 95)
            },
            "network": {
                "bytes_sent_total": network_sent_values[-1] - network_sent_values[0] if len(network_sent_values) > 1 else 0,
                "bytes_recv_total": network_recv_values[-1] - network_recv_values[0] if len(network_recv_values) > 1 else 0,
            },
            "sample_count": len(self.resource_history),
            "monitoring_duration_seconds": len(self.resource_history) * self.monitoring_interval
        }

    def _percentile(self, values: List[float], percentile: int) -> float:
        """Calculate percentile of values"""
        if not values:
            return 0.0
        values.sort()
        index = (percentile / 100) * (len(values) - 1)
        return values[int(index)]


class DatabaseOptimizer:
    """Database performance optimization"""

    def __init__(self):
        self.baseline_metrics: Optional[DatabasePerformanceMetrics] = None
        self.optimization_history: List[OptimizationResult] = []

    async def analyze_database_performance(self, connection_string: str) -> DatabasePerformanceMetrics:
        """Analyze database performance metrics"""
        # Simulate database performance analysis
        # In production, connect to actual database and collect metrics

        metrics = DatabasePerformanceMetrics(
            query_time_avg=45.2,
            query_time_p95=120.5,
            query_time_p99=250.8,
            connections_active=45,
            connections_idle=20,
            cache_hit_ratio=0.85,
            index_usage_ratio=0.92,
            slow_queries_count=3,
            deadlocks_count=0
        )

        if self.baseline_metrics is None:
            self.baseline_metrics = metrics

        return metrics

    def generate_database_optimizations(self, metrics: DatabasePerformanceMetrics) -> List[OptimizationRecommendation]:
        """Generate database optimization recommendations"""
        recommendations = []

        # Query performance optimizations
        if metrics.query_time_p95 > 100:
            recommendations.append(OptimizationRecommendation(
                recommendation_id="DB_OPT_001",
                target=OptimizationTarget.DATABASE,
                strategy=OptimizationStrategy.QUERY_OPTIMIZATION,
                description="Optimize slow queries with better indexing and query rewriting",
                expected_improvement=35.0,
                implementation_complexity="medium",
                risk_level="low",
                estimated_effort="2-4 hours",
                prerequisites=["Database access", "Query analysis tools"],
                steps=[
                    "Identify slow queries using EXPLAIN ANALYZE",
                    "Create missing indexes",
                    "Rewrite complex queries",
                    "Update ORM configurations",
                    "Test with production-like load"
                ],
                rollback_plan=[
                    "Remove new indexes",
                    "Revert query changes",
                    "Restore ORM configuration"
                ]
            ))

        # Connection pooling optimizations
        if metrics.connections_active > 50:
            recommendations.append(OptimizationRecommendation(
                recommendation_id="DB_OPT_002",
                target=OptimizationTarget.DATABASE,
                strategy=OptimizationStrategy.CONNECTION_POOLING,
                description="Implement connection pooling to reduce connection overhead",
                expected_improvement=25.0,
                implementation_complexity="low",
                risk_level="low",
                estimated_effort="1-2 hours",
                prerequisites=["Connection pool library", "Database configuration access"],
                steps=[
                    "Configure connection pool parameters",
                    "Update application database configuration",
                    "Monitor pool utilization",
                    "Adjust pool size based on load"
                ],
                rollback_plan=[
                    "Revert to direct connections",
                    "Remove connection pool configuration"
                ]
            ))

        # Cache optimizations
        if metrics.cache_hit_ratio < 0.8:
            recommendations.append(OptimizationRecommendation(
                recommendation_id="DB_OPT_003",
                target=OptimizationTarget.CACHE,
                strategy=OptimizationStrategy.CACHING,
                description="Implement query result caching to improve response times",
                expected_improvement=40.0,
                implementation_complexity="medium",
                risk_level="medium",
                estimated_effort="4-6 hours",
                prerequisites=["Redis/Memcached", "Cache invalidation strategy"],
                steps=[
                    "Identify cacheable queries",
                    "Implement caching layer",
                    "Set appropriate TTL values",
                    "Add cache invalidation logic",
                    "Monitor cache hit ratios"
                ],
                rollback_plan=[
                    "Disable caching layer",
                    "Clear cache data",
                    "Revert application code"
                ]
            ))

        # Index optimizations
        if metrics.index_usage_ratio < 0.9:
            recommendations.append(OptimizationRecommendation(
                recommendation_id="DB_OPT_004",
                target=OptimizationTarget.DATABASE,
                strategy=OptimizationStrategy.INDEX_OPTIMIZATION,
                description="Optimize database indexes for better query performance",
                expected_improvement=30.0,
                implementation_complexity="medium",
                risk_level="medium",
                estimated_effort="3-5 hours",
                prerequisites=["Database admin access", "Query analysis tools"],
                steps=[
                    "Analyze query patterns",
                    "Identify missing indexes",
                    "Create composite indexes",
                    "Remove unused indexes",
                    "Update statistics"
                ],
                rollback_plan=[
                    "Drop new indexes",
                    "Restore old index structure"
                ]
            ))

        return recommendations


class CacheOptimizer:
    """Cache performance optimization"""

    def __init__(self):
        self.cache_metrics_history: List[CachePerformanceMetrics] = []

    async def analyze_cache_performance(self, cache_endpoint: str) -> CachePerformanceMetrics:
        """Analyze cache performance metrics"""
        # Simulate cache performance analysis
        metrics = CachePerformanceMetrics(
            hit_ratio=0.78,
            miss_ratio=0.22,
            eviction_count=145,
            memory_usage_bytes=2147483648,  # 2GB
            operations_per_second=5000.0,
            average_response_time=0.5
        )

        self.cache_metrics_history.append(metrics)

        return metrics

    def generate_cache_optimizations(self, metrics: CachePerformanceMetrics) -> List[OptimizationRecommendation]:
        """Generate cache optimization recommendations"""
        recommendations = []

        # Hit ratio optimization
        if metrics.hit_ratio < 0.85:
            recommendations.append(OptimizationRecommendation(
                recommendation_id="CACHE_OPT_001",
                target=OptimizationTarget.CACHE,
                strategy=OptimizationStrategy.CACHING,
                description="Improve cache hit ratio through better key strategies and preloading",
                expected_improvement=25.0,
                implementation_complexity="medium",
                risk_level="low",
                estimated_effort="2-3 hours",
                prerequisites=["Cache access", "Application profiling"],
                steps=[
                    "Analyze cache access patterns",
                    "Implement intelligent preloading",
                    "Optimize cache key structure",
                    "Adjust TTL values",
                    "Monitor hit ratio improvements"
                ],
                rollback_plan=[
                    "Revert cache key structure",
                    "Remove preloading logic",
                    "Reset TTL values"
                ]
            ))

        # Memory optimization
        if metrics.eviction_count > 100:
            recommendations.append(OptimizationRecommendation(
                recommendation_id="CACHE_OPT_002",
                target=OptimizationTarget.MEMORY,
                strategy=OptimizationStrategy.RESOURCE_TUNING,
                description="Optimize cache memory allocation and eviction policies",
                expected_improvement=20.0,
                implementation_complexity="low",
                risk_level="low",
                estimated_effort="1-2 hours",
                prerequisites=["Cache configuration access", "Memory monitoring"],
                steps=[
                    "Analyze memory usage patterns",
                    "Adjust cache size limits",
                    "Configure eviction policies",
                    "Implement memory compression",
                    "Monitor eviction rates"
                ],
                rollback_plan=[
                    "Restore original cache configuration",
                    "Reset memory limits"
                ]
            ))

        return recommendations


class ApplicationOptimizer:
    """Application-level performance optimization"""

    def __init__(self):
        self.performance_profiles = {}

    async def profile_application_performance(self, application_url: str, duration_seconds: int = 300) -> Dict[str, Any]:
        """Profile application performance under load"""
        logger.info(f"Profiling application performance at {application_url}")

        # Simulate application profiling
        start_time = time.time()

        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(50):  # 50 concurrent requests
                task = self._make_request(session, application_url)
                tasks.append(task)

            results = await asyncio.gather(*tasks, return_exceptions=True)

        end_time = time.time()
        duration = end_time - start_time

        successful_requests = [r for r in results if not isinstance(r, Exception)]
        failed_requests = [r for r in results if isinstance(r, Exception)]

        if successful_requests:
            response_times = [r["response_time"] for r in successful_requests]
            status_codes = [r["status_code"] for r in successful_requests]

            profile = {
                "total_requests": len(tasks),
                "successful_requests": len(successful_requests),
                "failed_requests": len(failed_requests),
                "success_rate": len(successful_requests) / len(tasks) * 100,
                "requests_per_second": len(successful_requests) / duration,
                "response_time": {
                    "avg": statistics.mean(response_times),
                    "min": min(response_times),
                    "max": max(response_times),
                    "p95": self._percentile(response_times, 95),
                    "p99": self._percentile(response_times, 99)
                },
                "status_codes": {
                    "2xx": sum(1 for code in status_codes if 200 <= code < 300),
                    "4xx": sum(1 for code in status_codes if 400 <= code < 500),
                    "5xx": sum(1 for code in status_codes if 500 <= code < 600)
                },
                "duration_seconds": duration,
                "errors": [str(r) for r in failed_requests[:5]]  # First 5 errors
            }
        else:
            profile = {
                "total_requests": len(tasks),
                "successful_requests": 0,
                "failed_requests": len(failed_requests),
                "success_rate": 0,
                "errors": [str(r) for r in failed_requests[:5]]
            }

        return profile

    async def _make_request(self, session: aiohttp.ClientSession, url: str) -> Dict[str, Any]:
        """Make HTTP request and measure performance"""
        start_time = time.time()
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                await response.text()  # Read response body
                end_time = time.time()

                return {
                    "status_code": response.status,
                    "response_time": end_time - start_time,
                    "headers": dict(response.headers)
                }
        except Exception as e:
            end_time = time.time()
            return {
                "error": str(e),
                "response_time": end_time - start_time,
                "status_code": 0
            }

    def generate_application_optimizations(self, profile: Dict[str, Any]) -> List[OptimizationRecommendation]:
        """Generate application optimization recommendations"""
        recommendations = []

        # Response time optimizations
        avg_response_time = profile.get("response_time", {}).get("avg", 0)
        p95_response_time = profile.get("response_time", {}).get("p95", 0)

        if avg_response_time > 0.5:  # 500ms threshold
            recommendations.append(OptimizationRecommendation(
                recommendation_id="APP_OPT_001",
                target=OptimizationTarget.LATENCY,
                strategy=OptimizationStrategy.QUERY_OPTIMIZATION,
                description="Optimize application response times through code optimization and caching",
                expected_improvement=40.0,
                implementation_complexity="high",
                risk_level="medium",
                estimated_effort="8-12 hours",
                prerequisites=["Code access", "Profiling tools", "Load testing environment"],
                steps=[
                    "Profile application bottlenecks",
                    "Optimize database queries",
                    "Implement application-level caching",
                    "Optimize algorithms and data structures",
                    "Reduce external service calls",
                    "Implement async processing"
                ],
                rollback_plan=[
                    "Revert code changes",
                    "Disable new caching layers",
                    "Restore original algorithms"
                ]
            ))

        # Throughput optimizations
        requests_per_second = profile.get("requests_per_second", 0)
        if requests_per_second < 100:  # Low throughput threshold
            recommendations.append(OptimizationRecommendation(
                recommendation_id="APP_OPT_002",
                target=OptimizationTarget.THROUGHPUT,
                strategy=OptimizationStrategy.HORIZONTAL_SCALING,
                description="Increase application throughput through horizontal scaling",
                expected_improvement=60.0,
                implementation_complexity="medium",
                risk_level="low",
                estimated_effort="4-6 hours",
                prerequisites=["Load balancer", "Multiple servers", "Deployment automation"],
                steps=[
                    "Set up load balancer",
                    "Deploy application to multiple instances",
                    "Configure health checks",
                    "Test failover scenarios",
                    "Monitor load distribution"
                ],
                rollback_plan=[
                    "Remove extra instances",
                    "Disable load balancer",
                    "Restore single instance configuration"
                ]
            ))

        # Error rate optimizations
        success_rate = profile.get("success_rate", 100)
        if success_rate < 99:  # 99% success rate threshold
            recommendations.append(OptimizationRecommendation(
                recommendation_id="APP_OPT_003",
                target=OptimizationTarget.LATENCY,
                strategy=OptimizationStrategy.RESOURCE_TUNING,
                description="Improve application reliability and error handling",
                expected_improvement=30.0,
                implementation_complexity="medium",
                risk_level="low",
                estimated_effort="2-4 hours",
                prerequisites=["Error logs", "Monitoring tools", "Code access"],
                steps=[
                    "Analyze error patterns",
                    "Implement retry mechanisms",
                    "Add circuit breakers",
                    "Improve error logging",
                    "Add graceful degradation"
                ],
                rollback_plan=[
                    "Remove retry mechanisms",
                    "Disable circuit breakers",
                    "Restore original error handling"
                ]
            ))

        return recommendations

    def _percentile(self, values: List[float], percentile: int) -> float:
        """Calculate percentile of values"""
        if not values:
            return 0.0
        values.sort()
        index = (percentile / 100) * (len(values) - 1)
        return values[int(index)]


class ProductionOptimizer:
    """Comprehensive production performance optimization"""

    def __init__(self):
        self.resource_monitor = ResourceMonitor()
        self.database_optimizer = DatabaseOptimizer()
        self.cache_optimizer = CacheOptimizer()
        self.application_optimizer = ApplicationOptimizer()
        self.optimization_history: List[OptimizationResult] = []
        self.performance_baselines: Dict[str, PerformanceBaseline] = {}

    async def execute_optimization_assessment(self, production_config: Dict[str, Any]) -> Dict[str, Any]:
        """Execute comprehensive production optimization assessment"""
        logger.info("Starting production optimization assessment")

        assessment_results = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "environment": production_config.get("environment", "production"),
            "resource_analysis": await self._analyze_resources(),
            "database_analysis": await self._analyze_database(production_config),
            "cache_analysis": await self._analyze_cache(production_config),
            "application_analysis": await self._analyze_application(production_config),
            "optimization_recommendations": [],
            "performance_score": 0.0,
            "priority_actions": []
        }

        # Generate optimization recommendations
        all_recommendations = []
        all_recommendations.extend(assessment_results["database_analysis"]["recommendations"])
        all_recommendations.extend(assessment_results["cache_analysis"]["recommendations"])
        all_recommendations.extend(assessment_results["application_analysis"]["recommendations"])

        # Sort recommendations by expected improvement
        all_recommendations.sort(key=lambda x: x.expected_improvement, reverse=True)
        assessment_results["optimization_recommendations"] = all_recommendations

        # Generate priority actions (top 5 recommendations)
        assessment_results["priority_actions"] = [
            {
                "rank": i + 1,
                "recommendation": rec,
                "priority_score": self._calculate_priority_score(rec)
            }
            for i, rec in enumerate(all_recommendations[:5])
        ]

        # Calculate overall performance score
        assessment_results["performance_score"] = self._calculate_performance_score(assessment_results)

        return assessment_results

    async def _analyze_resources(self) -> Dict[str, Any]:
        """Analyze system resource utilization"""
        logger.info("Analyzing system resource utilization")

        # Monitor resources for 30 seconds
        resource_history = await self.resource_monitor.start_monitoring(30)
        resource_summary = self.resource_monitor.get_resource_summary()

        analysis = {
            "monitoring_duration": 30,
            "resource_summary": resource_summary,
            "utilization_status": self._assess_resource_utilization(resource_summary),
            "optimization_opportunities": self._identify_resource_optimizations(resource_summary),
            "recommendations": self._generate_resource_recommendations(resource_summary)
        }

        return analysis

    async def _analyze_database(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze database performance"""
        logger.info("Analyzing database performance")

        connection_string = config.get("database", {}).get("connection_string", "postgresql://localhost/cognee")

        # Analyze database metrics
        metrics = await self.database_optimizer.analyze_database_performance(connection_string)

        # Generate optimization recommendations
        recommendations = self.database_optimizer.generate_database_optimizations(metrics)

        analysis = {
            "current_metrics": asdict(metrics),
            "baseline_metrics": asdict(self.database_optimizer.baseline_metrics) if self.database_optimizer.baseline_metrics else None,
            "performance_comparison": self._compare_database_metrics(
                metrics,
                self.database_optimizer.baseline_metrics
            ),
            "recommendations": [asdict(rec) for rec in recommendations],
            "optimization_priority": self._prioritize_database_optimizations(recommendations)
        }

        return analysis

    async def _analyze_cache(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze cache performance"""
        logger.info("Analyzing cache performance")

        cache_endpoint = config.get("cache", {}).get("endpoint", "redis://localhost:6379")

        # Analyze cache metrics
        metrics = await self.cache_optimizer.analyze_cache_performance(cache_endpoint)

        # Generate optimization recommendations
        recommendations = self.cache_optimizer.generate_cache_optimizations(metrics)

        analysis = {
            "current_metrics": asdict(metrics),
            "historical_metrics": [asdict(m) for m in self.cache_optimizer.cache_metrics_history[-10:]],
            "recommendations": [asdict(rec) for rec in recommendations],
            "cache_efficiency_score": self._calculate_cache_efficiency_score(metrics),
            "optimization_priority": self._prioritize_cache_optimizations(recommendations)
        }

        return analysis

    async def _analyze_application(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze application performance"""
        logger.info("Analyzing application performance")

        application_url = config.get("application", {}).get("url", "http://localhost:8000")

        # Profile application performance
        performance_profile = await self.application_optimizer.profile_application_performance(
            application_url,
            duration_seconds=60
        )

        # Generate optimization recommendations
        recommendations = self.application_optimizer.generate_application_optimizations(performance_profile)

        analysis = {
            "performance_profile": performance_profile,
            "recommendations": [asdict(rec) for rec in recommendations],
            "application_health_score": self._calculate_application_health_score(performance_profile),
            "optimization_priority": self._prioritize_application_optimizations(recommendations)
        }

        return analysis

    def _assess_resource_utilization(self, resource_summary: Dict[str, Any]) -> Dict[str, str]:
        """Assess resource utilization status"""
        status = {}

        if "cpu" in resource_summary:
            cpu_avg = resource_summary["cpu"]["avg"]
            if cpu_avg < 50:
                status["cpu"] = "optimal"
            elif cpu_avg < 75:
                status["cpu"] = "moderate"
            else:
                status["cpu"] = "high"

        if "memory" in resource_summary:
            memory_avg = resource_summary["memory"]["avg"]
            if memory_avg < 70:
                status["memory"] = "optimal"
            elif memory_avg < 85:
                status["memory"] = "moderate"
            else:
                status["memory"] = "high"

        return status

    def _identify_resource_optimizations(self, resource_summary: Dict[str, Any]) -> List[str]:
        """Identify resource optimization opportunities"""
        opportunities = []

        if "cpu" in resource_summary:
            cpu_avg = resource_summary["cpu"]["avg"]
            cpu_p95 = resource_summary["cpu"]["p95"]

            if cpu_p95 > 80:
                opportunities.append("Consider CPU scaling or optimization")
            if cpu_avg > 60:
                opportunities.append("Monitor CPU usage patterns")

        if "memory" in resource_summary:
            memory_avg = resource_summary["memory"]["avg"]
            if memory_avg > 80:
                opportunities.append("Consider memory optimization or scaling")

        return opportunities

    def _generate_resource_recommendations(self, resource_summary: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate resource optimization recommendations"""
        recommendations = []

        # CPU optimizations
        if "cpu" in resource_summary:
            cpu_avg = resource_summary["cpu"]["avg"]
            if cpu_avg > 70:
                recommendations.append({
                    "type": "cpu",
                    "priority": "high",
                    "action": "optimize_cpu_usage",
                    "description": "High CPU utilization detected - consider optimization or scaling"
                })

        # Memory optimizations
        if "memory" in resource_summary:
            memory_avg = resource_summary["memory"]["avg"]
            if memory_avg > 80:
                recommendations.append({
                    "type": "memory",
                    "priority": "high",
                    "action": "optimize_memory_usage",
                    "description": "High memory usage detected - investigate memory leaks or increase resources"
                })

        return recommendations

    def _compare_database_metrics(self, current: DatabasePerformanceMetrics, baseline: Optional[DatabasePerformanceMetrics]) -> Dict[str, Any]:
        """Compare current database metrics with baseline"""
        if baseline is None:
            return {"status": "no_baseline"}

        comparison = {
            "query_time_change": ((current.query_time_avg - baseline.query_time_avg) / baseline.query_time_avg) * 100,
            "connection_change": current.connections_active - baseline.connections_active,
            "cache_hit_change": current.cache_hit_ratio - baseline.cache_hit_ratio,
            "slow_query_change": current.slow_queries_count - baseline.slow_queries_count
        }

        return comparison

    def _prioritize_database_optimizations(self, recommendations: List[OptimizationRecommendation]) -> List[Dict[str, Any]]:
        """Prioritize database optimizations"""
        prioritized = []
        for rec in recommendations:
            priority_score = self._calculate_priority_score(rec)
            prioritized.append({
                "recommendation": asdict(rec),
                "priority_score": priority_score,
                "implementation_order": self._get_implementation_order(rec)
            })

        prioritized.sort(key=lambda x: x["priority_score"], reverse=True)
        return prioritized

    def _prioritize_cache_optimizations(self, recommendations: List[OptimizationRecommendation]) -> List[Dict[str, Any]]:
        """Prioritize cache optimizations"""
        prioritized = []
        for rec in recommendations:
            priority_score = self._calculate_priority_score(rec)
            prioritized.append({
                "recommendation": asdict(rec),
                "priority_score": priority_score,
                "implementation_order": self._get_implementation_order(rec)
            })

        prioritized.sort(key=lambda x: x["priority_score"], reverse=True)
        return prioritized

    def _prioritize_application_optimizations(self, recommendations: List[OptimizationRecommendation]) -> List[Dict[str, Any]]:
        """Prioritize application optimizations"""
        prioritized = []
        for rec in recommendations:
            priority_score = self._calculate_priority_score(rec)
            prioritized.append({
                "recommendation": asdict(rec),
                "priority_score": priority_score,
                "implementation_order": self._get_implementation_order(rec)
            })

        prioritized.sort(key=lambda x: x["priority_score"], reverse=True)
        return prioritized

    def _calculate_priority_score(self, recommendation: OptimizationRecommendation) -> float:
        """Calculate priority score for recommendation"""
        # Factors: expected improvement, implementation complexity, risk level
        improvement_weight = 0.5
        complexity_weight = -0.3  # Negative because lower complexity is better
        risk_weight = -0.2  # Negative because lower risk is better

        # Convert categorical values to numeric
        complexity_scores = {"low": 1, "medium": 2, "high": 3}
        risk_scores = {"low": 1, "medium": 2, "high": 3}

        complexity_score = complexity_scores.get(recommendation.implementation_complexity, 2)
        risk_score = risk_scores.get(recommendation.risk_level, 2)

        priority_score = (
            recommendation.expected_improvement * improvement_weight +
            complexity_score * complexity_weight +
            risk_score * risk_weight
        )

        return max(priority_score, 0)  # Ensure non-negative

    def _get_implementation_order(self, recommendation: OptimizationRecommendation) -> int:
        """Get implementation order for recommendation"""
        if recommendation.risk_level == "low" and recommendation.implementation_complexity == "low":
            return 1  # Quick wins
        elif recommendation.expected_improvement > 40:
            return 2  # High impact
        elif recommendation.risk_level == "low":
            return 3  # Low risk
        else:
            return 4  # Standard

    def _calculate_cache_efficiency_score(self, metrics: CachePerformanceMetrics) -> float:
        """Calculate cache efficiency score"""
        hit_ratio_score = metrics.hit_ratio * 50  # 50% weight
        response_time_score = max(0, 10 - metrics.average_response_time) * 5  # 50% weight, inverted

        return hit_ratio_score + response_time_score

    def _calculate_application_health_score(self, profile: Dict[str, Any]) -> float:
        """Calculate application health score"""
        success_rate = profile.get("success_rate", 0) / 100
        avg_response_time = profile.get("response_time", {}).get("avg", 0)
        requests_per_second = profile.get("requests_per_second", 0)

        # Success rate (40% weight)
        success_score = success_rate * 40

        # Response time score (30% weight) - lower is better
        response_score = max(0, (2 - avg_response_time) * 15)

        # Throughput score (30% weight)
        throughput_score = min(30, requests_per_second * 0.3)

        return success_score + response_score + throughput_score

    def _calculate_performance_score(self, assessment_results: Dict[str, Any]) -> float:
        """Calculate overall performance score"""
        scores = []

        # Resource utilization score
        resource_analysis = assessment_results.get("resource_analysis", {})
        resource_status = resource_analysis.get("utilization_status", {})

        if resource_status:
            resource_score = 0
            for component, status in resource_status.items():
                if status == "optimal":
                    resource_score += 25
                elif status == "moderate":
                    resource_score += 15
                else:
                    resource_score += 5
            scores.append(min(resource_score, 100))

        # Database performance score
        db_analysis = assessment_results.get("database_analysis", {})
        db_recommendations = db_analysis.get("recommendations", [])
        db_score = max(0, 100 - len(db_recommendations) * 20)
        scores.append(db_score)

        # Cache performance score
        cache_analysis = assessment_results.get("cache_analysis", {})
        cache_score = cache_analysis.get("cache_efficiency_score", 50)
        scores.append(cache_score)

        # Application performance score
        app_analysis = assessment_results.get("application_analysis", {})
        app_score = app_analysis.get("application_health_score", 50)
        scores.append(app_score)

        return statistics.mean(scores) if scores else 50.0

    async def apply_optimization(self, recommendation: OptimizationRecommendation) -> OptimizationResult:
        """Apply optimization recommendation"""
        logger.info(f"Applying optimization: {recommendation.recommendation_id}")

        optimization_id = f"opt_{int(time.time())}"
        start_time = datetime.now(timezone.utc)

        # Collect before metrics
        before_metrics = await self._collect_optimization_metrics(recommendation.target)

        # Apply optimization based on strategy
        try:
            success = await self._implement_optimization(recommendation)

            if success:
                # Wait for optimization to take effect
                await asyncio.sleep(5)

                # Collect after metrics
                after_metrics = await self._collect_optimization_metrics(recommendation.target)

                # Calculate improvement
                improvement_percentage = self._calculate_improvement(before_metrics, after_metrics, recommendation.target)

                result = OptimizationResult(
                    optimization_id=optimization_id,
                    recommendation_id=recommendation.recommendation_id,
                    target=recommendation.target,
                    strategy=recommendation.strategy,
                    before_metrics=before_metrics,
                    after_metrics=after_metrics,
                    improvement_percentage=improvement_percentage,
                    implementation_time=datetime.now(timezone.utc) - start_time,
                    success=True
                )
            else:
                result = OptimizationResult(
                    optimization_id=optimization_id,
                    recommendation_id=recommendation.recommendation_id,
                    target=recommendation.target,
                    strategy=recommendation.strategy,
                    before_metrics=before_metrics,
                    after_metrics={},
                    improvement_percentage=0.0,
                    implementation_time=datetime.now(timezone.utc) - start_time,
                    success=False,
                    side_effects=["Optimization implementation failed"]
                )

        except Exception as e:
            result = OptimizationResult(
                optimization_id=optimization_id,
                recommendation_id=recommendation.recommendation_id,
                target=recommendation.target,
                strategy=recommendation.strategy,
                before_metrics=before_metrics,
                after_metrics={},
                improvement_percentage=0.0,
                implementation_time=datetime.now(timezone.utc) - start_time,
                success=False,
                side_effects=[f"Exception during implementation: {str(e)}"]
            )

        self.optimization_history.append(result)
        return result

    async def _collect_optimization_metrics(self, target: OptimizationTarget) -> Dict[str, float]:
        """Collect metrics for optimization target"""
        if target == OptimizationTarget.DATABASE:
            metrics = await self.database_optimizer.analyze_database_performance("")
            return asdict(metrics)
        elif target == OptimizationTarget.CACHE:
            metrics = await self.cache_optimizer.analyze_cache_performance("")
            return asdict(metrics)
        elif target in [OptimizationTarget.CPU, OptimizationTarget.MEMORY]:
            resource_summary = self.resource_monitor.get_resource_summary()
            return resource_summary.get(target.value, {})
        else:
            # For other targets, collect general resource metrics
            resource_summary = self.resource_monitor.get_resource_summary()
            return resource_summary

    async def _implement_optimization(self, recommendation: OptimizationRecommendation) -> bool:
        """Implement optimization based on recommendation"""
        # Simulate optimization implementation
        logger.info(f"Implementing {recommendation.strategy.value} optimization for {recommendation.target.value}")

        # Simulate implementation delay
        await asyncio.sleep(1)

        # Simulate success probability based on complexity
        success_probability = {
            "low": 0.95,
            "medium": 0.85,
            "high": 0.70
        }

        import random
        prob = success_probability.get(recommendation.implementation_complexity, 0.8)
        return random.random() < prob

    def _calculate_improvement(self, before: Dict[str, float], after: Dict[str, float], target: OptimizationTarget) -> float:
        """Calculate improvement percentage"""
        if not before or not after:
            return 0.0

        # Different metrics for different targets
        if target == OptimizationTarget.DATABASE:
            # For database, lower query times are better
            before_time = before.get("query_time_avg", 0)
            after_time = after.get("query_time_avg", 0)
            if before_time > 0:
                return ((before_time - after_time) / before_time) * 100
        elif target == OptimizationTarget.CACHE:
            # For cache, higher hit ratio is better
            before_hit = before.get("hit_ratio", 0)
            after_hit = after.get("hit_ratio", 0)
            return ((after_hit - before_hit) / before_hit * 100) if before_hit > 0 else 0
        elif target == OptimizationTarget.LATENCY:
            # For latency, lower response times are better
            before_response = before.get("avg", 0)
            after_response = after.get("avg", 0)
            if before_response > 0:
                return ((before_response - after_response) / before_response) * 100
        elif target == OptimizationTarget.THROUGHPUT:
            # For throughput, higher RPS is better
            before_rps = before.get("requests_per_second", 0)
            after_rps = after.get("requests_per_second", 0)
            return ((after_rps - before_rps) / before_rps * 100) if before_rps > 0 else 0

        return 0.0


# Pytest test fixtures and tests
@pytest.fixture
async def production_optimizer():
    """Production optimizer fixture"""
    return ProductionOptimizer()


@pytest.fixture
async def production_configs():
    """Production optimization configurations"""
    return [
        {
            "config_id": "opt_config_001",
            "name": "Production Optimization",
            "environment": "production",
            "database": {
                "connection_string": "postgresql://localhost/cognee",
                "type": "postgresql"
            },
            "cache": {
                "endpoint": "redis://localhost:6379",
                "type": "redis"
            },
            "application": {
                "url": "http://localhost:8000",
                "type": "web_api"
            }
        },
        {
            "config_id": "opt_config_002",
            "name": "High Load Optimization",
            "environment": "production",
            "database": {
                "connection_string": "postgresql://localhost/cognee",
                "type": "postgresql"
            },
            "cache": {
                "endpoint": "redis://localhost:6379",
                "type": "redis"
            },
            "application": {
                "url": "http://localhost:8000",
                "type": "web_api"
            },
            "load_balancing": {
                "enabled": True,
                "instances": 3
            }
        }
    ]


@pytest.mark.production
@pytest.mark.optimization
async def test_resource_monitoring(production_optimizer):
    """Test system resource monitoring"""
    resource_monitor = production_optimizer.resource_monitor

    # Test resource collection
    resource_history = await resource_monitor.start_monitoring(5)  # 5 seconds

    assert len(resource_history) > 0, "Resource history should contain samples"

    # Test resource summary
    summary = resource_monitor.get_resource_summary()
    assert "cpu" in summary, "CPU metrics should be included"
    assert "memory" in summary, "Memory metrics should be included"
    assert "sample_count" in summary, "Sample count should be recorded"


@pytest.mark.production
@pytest.mark.optimization
async def test_database_optimization(production_optimizer):
    """Test database performance optimization"""
    database_optimizer = production_optimizer.database_optimizer

    # Test database performance analysis
    metrics = await database_optimizer.analyze_database_performance("test_connection")
    assert metrics.query_time_avg > 0, "Average query time should be positive"
    assert metrics.cache_hit_ratio >= 0, "Cache hit ratio should be non-negative"

    # Test optimization recommendations
    recommendations = database_optimizer.generate_database_optimizations(metrics)
    assert isinstance(recommendations, list), "Recommendations should be a list"

    if recommendations:
        rec = recommendations[0]
        assert rec.target == OptimizationTarget.DATABASE, "Target should be database"
        assert rec.expected_improvement > 0, "Expected improvement should be positive"


@pytest.mark.production
@pytest.mark.optimization
async def test_cache_optimization(production_optimizer):
    """Test cache performance optimization"""
    cache_optimizer = production_optimizer.cache_optimizer

    # Test cache performance analysis
    metrics = await cache_optimizer.analyze_cache_performance("redis://localhost")
    assert 0 <= metrics.hit_ratio <= 1, "Hit ratio should be between 0 and 1"
    assert metrics.operations_per_second >= 0, "Operations per second should be non-negative"

    # Test optimization recommendations
    recommendations = cache_optimizer.generate_cache_optimizations(metrics)
    assert isinstance(recommendations, list), "Recommendations should be a list"

    if recommendations:
        rec = recommendations[0]
        assert rec.target in [OptimizationTarget.CACHE, OptimizationTarget.MEMORY], "Target should be cache or memory"


@pytest.mark.production
@pytest.mark.optimization
async def test_application_optimization(production_optimizer):
    """Test application performance optimization"""
    application_optimizer = production_optimizer.application_optimizer

    # Test application profiling
    profile = await application_optimizer.profile_application_performance(
        "http://httpbin.org/delay/0.1",  # Use a test endpoint
        duration_seconds=10
    )

    assert profile["total_requests"] > 0, "Should make requests"
    assert "success_rate" in profile, "Success rate should be calculated"
    assert "response_time" in profile, "Response time should be measured"

    # Test optimization recommendations
    recommendations = application_optimizer.generate_application_optimizations(profile)
    assert isinstance(recommendations, list), "Recommendations should be a list"


@pytest.mark.production
@pytest.mark.optimization
async def test_comprehensive_optimization_assessment(production_optimizer, production_configs):
    """Test comprehensive production optimization assessment"""
    config = production_configs[0]

    # Execute full optimization assessment
    assessment_results = await production_optimizer.execute_optimization_assessment(config)

    # Verify all analysis components
    expected_components = [
        "resource_analysis",
        "database_analysis",
        "cache_analysis",
        "application_analysis",
        "optimization_recommendations",
        "performance_score"
    ]

    for component in expected_components:
        assert component in assessment_results, f"Component {component} should be included"

    # Verify resource analysis
    resource_analysis = assessment_results["resource_analysis"]
    assert resource_analysis["monitoring_duration"] == 30, "Resource monitoring duration should be 30 seconds"
    assert "resource_summary" in resource_analysis, "Resource summary should be included"

    # Verify database analysis
    database_analysis = assessment_results["database_analysis"]
    assert "current_metrics" in database_analysis, "Current database metrics should be included"
    assert "recommendations" in database_analysis, "Database recommendations should be included"

    # Verify cache analysis
    cache_analysis = assessment_results["cache_analysis"]
    assert "current_metrics" in cache_analysis, "Current cache metrics should be included"
    assert "cache_efficiency_score" in cache_analysis, "Cache efficiency score should be calculated"

    # Verify application analysis
    application_analysis = assessment_results["application_analysis"]
    assert "performance_profile" in application_analysis, "Application performance profile should be included"
    assert "application_health_score" in application_analysis, "Application health score should be calculated"

    # Verify optimization recommendations
    recommendations = assessment_results["optimization_recommendations"]
    assert isinstance(recommendations, list), "Optimization recommendations should be a list"

    # Verify priority actions
    priority_actions = assessment_results["priority_actions"]
    assert len(priority_actions) <= 5, "Should have at most 5 priority actions"
    assert all(action["rank"] <= 5 for action in priority_actions), "Action ranks should be <= 5"

    # Verify performance score
    performance_score = assessment_results["performance_score"]
    assert 0 <= performance_score <= 100, "Performance score should be between 0 and 100"


@pytest.mark.production
@pytest.mark.optimization
async def test_optimization_application(production_optimizer):
    """Test optimization application"""
    # Create a test recommendation
    recommendation = OptimizationRecommendation(
        recommendation_id="TEST_OPT_001",
        target=OptimizationTarget.DATABASE,
        strategy=OptimizationStrategy.QUERY_OPTIMIZATION,
        description="Test optimization for database query performance",
        expected_improvement=25.0,
        implementation_complexity="low",
        risk_level="low",
        estimated_effort="1 hour"
    )

    # Apply optimization
    result = await production_optimizer.apply_optimization(recommendation)

    # Verify optimization result
    assert result.optimization_id is not None, "Optimization ID should be generated"
    assert result.recommendation_id == recommendation.recommendation_id, "Recommendation ID should match"
    assert result.target == recommendation.target, "Target should match"
    assert result.strategy == recommendation.strategy, "Strategy should match"
    assert result.implementation_time.total_seconds() > 0, "Implementation time should be positive"

    # Verify optimization was added to history
    assert len(production_optimizer.optimization_history) > 0, "Optimization should be added to history"


@pytest.mark.production
@pytest.mark.optimization
async def test_performance_scoring(production_optimizer):
    """Test performance scoring calculations"""
    # Test cache efficiency score
    cache_metrics = CachePerformanceMetrics(
        hit_ratio=0.85,
        miss_ratio=0.15,
        eviction_count=100,
        memory_usage_bytes=1073741824,
        operations_per_second=5000.0,
        average_response_time=0.5
    )

    cache_score = production_optimizer._calculate_cache_efficiency_score(cache_metrics)
    assert 0 <= cache_score <= 100, "Cache efficiency score should be between 0 and 100"

    # Test application health score
    profile = {
        "success_rate": 99.5,
        "response_time": {"avg": 0.8},
        "requests_per_second": 150
    }

    app_score = production_optimizer._calculate_application_health_score(profile)
    assert 0 <= app_score <= 100, "Application health score should be between 0 and 100"

    # Test priority score calculation
    recommendation = OptimizationRecommendation(
        recommendation_id="TEST_OPT_002",
        target=OptimizationTarget.LATENCY,
        strategy=OptimizationStrategy.CACHING,
        description="Test recommendation",
        expected_improvement=30.0,
        implementation_complexity="medium",
        risk_level="low",
        estimated_effort="2 hours"
    )

    priority_score = production_optimizer._calculate_priority_score(recommendation)
    assert priority_score >= 0, "Priority score should be non-negative"


@pytest.mark.production
@pytest.mark.optimization
async def test_optimization_prioritization(production_optimizer):
    """Test optimization recommendation prioritization"""
    # Create test recommendations with different characteristics
    recommendations = [
        OptimizationRecommendation(
            recommendation_id="OPT_001",
            target=OptimizationTarget.DATABASE,
            strategy=OptimizationStrategy.QUERY_OPTIMIZATION,
            description="High impact, low complexity",
            expected_improvement=40.0,
            implementation_complexity="low",
            risk_level="low",
            estimated_effort="1 hour"
        ),
        OptimizationRecommendation(
            recommendation_id="OPT_002",
            target=OptimizationTarget.LATENCY,
            strategy=OptimizationStrategy.CACHING,
            description="Medium impact, medium complexity",
            expected_improvement=25.0,
            implementation_complexity="medium",
            risk_level="medium",
            estimated_effort="4 hours"
        )
    ]

    # Test database optimization prioritization
    db_prioritized = production_optimizer._prioritize_database_optimizations(recommendations)
    assert len(db_prioritized) == len(recommendations), "All recommendations should be prioritized"

    # Should be sorted by priority score (descending)
    for i in range(1, len(db_prioritized)):
        assert (
            db_prioritized[i-1]["priority_score"] >= db_prioritized[i]["priority_score"]
        ), "Should be sorted by priority score"

    # Test implementation order assignment
    for item in db_prioritized:
        rec = item["recommendation"]
        implementation_order = item["implementation_order"]

        if rec["implementation_complexity"] == "low" and rec["risk_level"] == "low":
            assert implementation_order == 1, "Quick wins should have order 1"
        elif rec["expected_improvement"] > 40:
            assert implementation_order == 2, "High impact should have order 2"


if __name__ == "__main__":
    # Run production optimization validation
    print("=" * 60)
    print("PRODUCTION PERFORMANCE OPTIMIZATION VALIDATION")
    print("=" * 60)

    async def main():
        optimizer = ProductionOptimizer()

        print("\n--- Testing Resource Monitoring ---")
        resource_history = await optimizer.resource_monitor.start_monitoring(5)
        resource_summary = optimizer.resource_monitor.get_resource_summary()
        print(f"✓ Collected {len(resource_history)} resource samples")
        print(f"✓ CPU utilization: {resource_summary.get('cpu', {}).get('avg', 0):.1f}%")
        print(f"✓ Memory utilization: {resource_summary.get('memory', {}).get('avg', 0):.1f}%")

        print("\n--- Testing Database Optimization ---")
        db_metrics = await optimizer.database_optimizer.analyze_database_performance("test_connection")
        db_recommendations = optimizer.database_optimizer.generate_database_optimizations(db_metrics)
        print(f"✓ Query time average: {db_metrics.query_time_avg:.1f}ms")
        print(f"✓ Cache hit ratio: {db_metrics.cache_hit_ratio:.2%}")
        print(f"✓ Database recommendations: {len(db_recommendations)}")

        print("\n--- Testing Cache Optimization ---")
        cache_metrics = await optimizer.cache_optimizer.analyze_cache_performance("redis://localhost")
        cache_recommendations = optimizer.cache_optimizer.generate_cache_optimizations(cache_metrics)
        cache_efficiency = optimizer._calculate_cache_efficiency_score(cache_metrics)
        print(f"✓ Cache hit ratio: {cache_metrics.hit_ratio:.2%}")
        print(f"✓ Operations per second: {cache_metrics.operations_per_second:.0f}")
        print(f"✓ Cache efficiency score: {cache_efficiency:.1f}")
        print(f"✓ Cache recommendations: {len(cache_recommendations)}")

        print("\n--- Testing Application Optimization ---")
        app_profile = await optimizer.application_optimizer.profile_application_performance(
            "http://httpbin.org/delay/0.1", duration_seconds=10
        )
        app_recommendations = optimizer.application_optimizer.generate_application_optimizations(app_profile)
        app_health = optimizer._calculate_application_health_score(app_profile)
        print(f"✓ Application success rate: {app_profile.get('success_rate', 0):.1f}%")
        print(f"✓ Average response time: {app_profile.get('response_time', {}).get('avg', 0):.3f}s")
        print(f"✓ Application health score: {app_health:.1f}")
        print(f"✓ Application recommendations: {len(app_recommendations)}")

        print("\n--- Testing Comprehensive Optimization Assessment ---")
        config = {
            "config_id": "test_config",
            "environment": "test",
            "database": {"connection_string": "postgresql://localhost/cognee"},
            "cache": {"endpoint": "redis://localhost:6379"},
            "application": {"url": "http://localhost:8000"}
        }

        assessment = await optimizer.execute_optimization_assessment(config)
        performance_score = assessment["performance_score"]
        priority_actions = assessment["priority_actions"]

        print(f"✓ Overall performance score: {performance_score:.1f}/100")
        print(f"✓ Total recommendations: {len(assessment['optimization_recommendations'])}")
        print(f"✓ Priority actions identified: {len(priority_actions)}")

        if priority_actions:
            print("\nTop Priority Actions:")
            for action in priority_actions[:3]:
                rec = action["recommendation"]
                print(f"  {action['rank']}. {rec['description']}")
                print(f"     Expected improvement: {rec['expected_improvement']:.0f}%")
                print(f"     Implementation: {rec['implementation_complexity']} complexity, {rec['estimated_effort']}")

        print("\n--- Testing Optimization Application ---")
        if assessment["optimization_recommendations"]:
            # Apply first recommendation
            first_rec_data = assessment["optimization_recommendations"][0]
            recommendation = OptimizationRecommendation(
                recommendation_id=first_rec_data["recommendation_id"],
                target=OptimizationTarget(first_rec_data["target"]),
                strategy=OptimizationStrategy(first_rec_data["strategy"]),
                description=first_rec_data["description"],
                expected_improvement=first_rec_data["expected_improvement"],
                implementation_complexity=first_rec_data["implementation_complexity"],
                risk_level=first_rec_data["risk_level"],
                estimated_effort=first_rec_data["estimated_effort"]
            )

            result = await optimizer.apply_optimization(recommendation)
            print(f"✓ Optimization ID: {result.optimization_id}")
            print(f"✓ Success: {result.success}")
            print(f"✓ Implementation time: {result.implementation_time.total_seconds():.1f}s")
            if result.success:
                print(f"✓ Measured improvement: {result.improvement_percentage:.1f}%")

        print("\n" + "=" * 60)
        print("PRODUCTION PERFORMANCE OPTIMIZATION VALIDATION COMPLETED")
        print("=" * 60)

    asyncio.run(main())