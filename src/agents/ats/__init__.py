"""
ATS (Algorithmic Trading System) Agents
Category containing 7 trading-focused agents
"""

from .algorithmic_trading_system import AlgorithmicTradingSystem
from .risk_management import RiskManagement
from .ats_memory_wrapper import ATSMemoryWrapper

__all__ = [
    "AlgorithmicTradingSystem",
    "RiskManagement",
    "ATSMemoryWrapper"
]

# ATS Agents Registry
ATS_AGENTS = {
    "algorithmic-trading-system": {
        "class": AlgorithmicTradingSystem,
        "description": "High-frequency trading and market analysis",
        "capabilities": ["market_analysis", "signal_generation", "order_execution"],
        "critical": True
    },
    "risk-management": {
        "class": RiskManagement,
        "description": "Risk assessment and position monitoring",
        "capabilities": ["risk_assessment", "position_monitoring", "compliance_check"],
        "critical": True
    },
    "portfolio-optimizer": {
        "description": "Portfolio optimization and allocation",
        "capabilities": ["portfolio_optimization", "allocation_analysis", "performance_tracking"],
        "critical": False
    },
    "market-analyzer": {
        "description": "Market data analysis and trend detection",
        "capabilities": ["market_data_analysis", "trend_detection", "sentiment_analysis"],
        "critical": False
    },
    "execution-engine": {
        "description": "Trade execution and order management",
        "capabilities": ["order_execution", "trade_confirmation", "settlement"],
        "critical": True
    },
    "signal-processor": {
        "description": "Signal validation and enrichment",
        "capabilities": ["signal_validation", "signal_enrichment", "signal_routing"],
        "critical": False
    },
    "compliance-monitor": {
        "description": "Regulatory compliance and monitoring",
        "capabilities": ["regulatory_monitoring", "compliance_reporting", "audit_trail"],
        "critical": True
    }
}

async def create_ats_agent(agent_id: str, memory_integration):
    """Factory function to create ATS agents"""
    if agent_id not in ATS_AGENTS:
        raise ValueError(f"Unknown ATS agent: {agent_id}")

    agent_info = ATS_AGENTS[agent_id]
    agent_class = agent_info.get("class")

    if agent_class:
        return await agent_class(memory_integration)
    else:
        # For agents not yet implemented
        return None