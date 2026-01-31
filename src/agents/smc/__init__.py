"""
SMC (Shared Multi-Agent Components) Agents
Category containing 6 coordination and infrastructure focused agents
"""

from .context_manager import ContextManager
from .smc_memory_wrapper import SMCMemoryWrapper

__all__ = [
    "ContextManager",
    "SMCMemoryWrapper"
]

# SMC Agents Registry
SMC_AGENTS = {
    "context-manager": {
        "class": ContextManager,
        "description": "Context management and sharing across agents",
        "capabilities": ["context_sharing", "session_management", "state_tracking"],
        "critical": True
    },
    "knowledge-graph": {
        "description": "Knowledge management and semantic search",
        "capabilities": ["knowledge_management", "semantic_search", "relationship_mapping"],
        "critical": True
    },
    "message-broker": {
        "description": "Message routing and communication protocol",
        "capabilities": ["message_routing", "communication_protocol", "queue_management"],
        "critical": True
    },
    "task-scheduler": {
        "description": "Task scheduling and resource allocation",
        "capabilities": ["task_scheduling", "resource_allocation", "workflow_management"],
        "critical": True
    },
    "data-processor": {
        "description": "Data transformation and batch processing",
        "capabilities": ["data_transformation", "batch_processing", "stream_processing"],
        "critical": False
    },
    "api-gateway": {
        "description": "API management and request routing",
        "capabilities": ["api_management", "rate_limiting", "request_routing"],
        "critical": True
    }
}

async def create_smc_agent(agent_id: str, memory_integration):
    """Factory function to create SMC agents"""
    if agent_id not in SMC_AGENTS:
        raise ValueError(f"Unknown SMC agent: {agent_id}")

    agent_info = SMC_AGENTS[agent_id]
    agent_class = agent_info.get("class")

    if agent_class:
        return await agent_class(memory_integration)
    else:
        # For agents not yet implemented
        return None