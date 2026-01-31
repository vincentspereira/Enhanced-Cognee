"""
OMA (Other Multi-Agent) Agents
Category containing 10 development and operations focused agents
"""

from .code_reviewer import CodeReviewer
from .oma_memory_wrapper import OMAMemoryWrapper

__all__ = [
    "CodeReviewer",
    "OMAMemoryWrapper"
]

# OMA Agents Registry
OMA_AGENTS = {
    "code-reviewer": {
        "class": CodeReviewer,
        "description": "Code review and quality analysis",
        "capabilities": ["code_analysis", "quality_check", "security_audit"],
        "critical": False
    },
    "data-engineer": {
        "description": "Data pipeline and ETL processes",
        "capabilities": ["data_pipeline", "etl_process", "data_quality"],
        "critical": False
    },
    "debug-specialist": {
        "description": "Bug analysis and error resolution",
        "capabilities": ["bug_analysis", "error_resolution", "performance_debugging"],
        "critical": False
    },
    "frontend-developer": {
        "description": "UI development and frontend optimization",
        "capabilities": ["ui_development", "frontend_optimization", "user_experience"],
        "critical": False
    },
    "backend-developer": {
        "description": "API development and backend services",
        "capabilities": ["api_development", "backend_optimization", "database_design"],
        "critical": False
    },
    "security-specialist": {
        "description": "Security analysis and vulnerability assessment",
        "capabilities": ["security_analysis", "vulnerability_assessment", "penetration_testing"],
        "critical": False
    },
    "test-engineer": {
        "description": "Test automation and quality assurance",
        "capabilities": ["test_automation", "quality_assurance", "performance_testing"],
        "critical": False
    },
    "technical-writer": {
        "description": "Documentation and knowledge management",
        "capabilities": ["documentation", "api_docs", "user_guides"],
        "critical": False
    },
    "devops-engineer": {
        "description": "Infrastructure and deployment automation",
        "capabilities": ["deployment", "infrastructure", "monitoring"],
        "critical": False
    },
    "ui-ux-designer": {
        "description": "Design system and user research",
        "capabilities": ["design_system", "user_research", "prototyping"],
        "critical": False
    }
}

async def create_oma_agent(agent_id: str, memory_integration):
    """Factory function to create OMA agents"""
    if agent_id not in OMA_AGENTS:
        raise ValueError(f"Unknown OMA agent: {agent_id}")

    agent_info = OMA_AGENTS[agent_id]
    agent_class = agent_info.get("class")

    if agent_class:
        return await agent_class(memory_integration)
    else:
        # For agents not yet implemented
        return None