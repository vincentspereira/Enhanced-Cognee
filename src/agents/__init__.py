"""
Enhanced Cognee Agents System
Comprehensive agent architecture with 21 sub-agents across ATS/OMA/SMC categories
"""

from . import ats
from . import oma
from . import smc
from ..agent_memory_integration import AgentMemoryIntegration

__all__ = [
    "ats",
    "oma",
    "smc",
    "AgentRegistry",
    "create_agent"
]

# Complete Agent Registry
ALL_AGENTS = {
    **ats.ATS_AGENTS,
    **oma.OMA_AGENTS,
    **smc.SMC_AGENTS
}

# Agent Categories
AGENT_CATEGORIES = {
    "ATS": {
        "name": "Algorithmic Trading System",
        "description": "Trading and market analysis focused agents",
        "agents": list(ats.ATS_AGENTS.keys()),
        "count": len(ats.ATS_AGENTS)
    },
    "OMA": {
        "name": "Other Multi-Agent",
        "description": "Development and operations focused agents",
        "agents": list(oma.OMA_AGENTS.keys()),
        "count": len(oma.OMA_AGENTS)
    },
    "SMC": {
        "name": "Shared Multi-Agent Components",
        "description": "Coordination and infrastructure focused agents",
        "agents": list(smc.SMC_AGENTS.keys()),
        "count": len(smc.SMC_AGENTS)
    }
}

class AgentRegistry:
    """
    Central registry for managing all 21 agents across categories
    """

    def __init__(self, memory_integration: AgentMemoryIntegration):
        self.memory_integration = memory_integration
        self.agent_instances = {}
        self.category_factories = {
            "ATS": ats.create_ats_agent,
            "OMA": oma.create_oma_agent,
            "SMC": smc.create_smc_agent
        }

    async def initialize_critical_agents(self):
        """Initialize all critical agents"""
        critical_agents = [
            agent_id for agent_id, info in ALL_AGENTS.items()
            if info.get("critical", False)
        ]

        initialized_agents = []
        for agent_id in critical_agents:
            try:
                agent = await self.create_agent(agent_id)
                if agent:
                    self.agent_instances[agent_id] = agent
                    initialized_agents.append(agent_id)
                    print(f"Initialized critical agent: {agent_id}")
            except Exception as e:
                print(f"Failed to initialize critical agent {agent_id}: {e}")

        return initialized_agents

    async def create_agent(self, agent_id: str):
        """Create a specific agent by ID"""
        if agent_id not in ALL_AGENTS:
            raise ValueError(f"Unknown agent: {agent_id}")

        # Determine category
        agent_category = None
        for category, agents in AGENT_CATEGORIES.items():
            if agent_id in agents["agents"]:
                agent_category = category
                break

        if not agent_category:
            raise ValueError(f"Could not determine category for agent: {agent_id}")

        # Use category factory
        factory = self.category_factories[agent_category]
        return await factory(agent_id, self.memory_integration)

    async def get_agent(self, agent_id: str):
        """Get an existing agent instance"""
        if agent_id not in self.agent_instances:
            # Try to create it
            agent = await self.create_agent(agent_id)
            if agent:
                self.agent_instances[agent_id] = agent

        return self.agent_instances.get(agent_id)

    async def create_category_agents(self, category: str):
        """Create all agents in a specific category"""
        if category not in AGENT_CATEGORIES:
            raise ValueError(f"Unknown category: {category}")

        category_info = AGENT_CATEGORIES[category]
        created_agents = []

        for agent_id in category_info["agents"]:
            try:
                agent = await self.create_agent(agent_id)
                if agent:
                    self.agent_instances[agent_id] = agent
                    created_agents.append(agent_id)
            except Exception as e:
                print(f"Failed to create agent {agent_id}: {e}")

        return created_agents

    def get_agent_info(self, agent_id: str):
        """Get information about an agent"""
        return ALL_AGENTS.get(agent_id)

    def get_category_info(self, category: str):
        """Get information about a category"""
        return AGENT_CATEGORIES.get(category)

    def list_all_agents(self):
        """List all available agents"""
        return ALL_AGENTS

    def list_agents_by_category(self, category: str):
        """List agents in a specific category"""
        category_info = AGENT_CATEGORIES.get(category)
        return category_info["agents"] if category_info else []

    def get_critical_agents(self):
        """Get list of critical agents"""
        return [
            agent_id for agent_id, info in ALL_AGENTS.items()
            if info.get("critical", False)
        ]

    async def shutdown_all_agents(self):
        """Shutdown all agent instances"""
        for agent_id, agent in self.agent_instances.items():
            try:
                if hasattr(agent, 'shutdown'):
                    await agent.shutdown()
                elif hasattr(agent, 'close'):
                    await agent.close()
                print(f"Shutdown agent: {agent_id}")
            except Exception as e:
                print(f"Error shutting down agent {agent_id}: {e}")

        self.agent_instances.clear()

# Factory function
async def create_agent(agent_id: str, memory_integration: AgentMemoryIntegration):
    """
    Create an agent by ID

    Args:
        agent_id: The ID of the agent to create
        memory_integration: AgentMemoryIntegration instance

    Returns:
        Agent instance or None if not implemented
    """
    registry = AgentRegistry(memory_integration)
    return await registry.create_agent(agent_id)

async def create_critical_agents(memory_integration: AgentMemoryIntegration):
    """
    Create all critical agents

    Args:
        memory_integration: AgentMemoryIntegration instance

    Returns:
        List of initialized critical agent IDs
    """
    registry = AgentRegistry(memory_integration)
    return await registry.initialize_critical_agents()

def get_agent_system_info():
    """Get comprehensive information about the agent system"""
    total_agents = len(ALL_AGENTS)
    critical_agents = len([info for info in ALL_AGENTS.values() if info.get("critical", False)])

    return {
        "total_agents": total_agents,
        "critical_agents": critical_agents,
        "categories": AGENT_CATEGORIES,
        "agents": ALL_AGENTS
    }

if __name__ == "__main__":
    # Example usage
    async def example_usage():
        from ..agent_memory_integration import AgentMemoryIntegration

        integration = AgentMemoryIntegration()
        await integration.initialize()

        # Create registry
        registry = AgentRegistry(integration)

        # Initialize critical agents
        critical_agents = await registry.initialize_critical_agents()
        print(f"Initialized {len(critical_agents)} critical agents")

        # Create specific agent
        trading_agent = await registry.get_agent("algorithmic-trading-system")
        if trading_agent:
            print(f"Trading agent created: {type(trading_agent).__name__}")

        # Get system info
        system_info = get_agent_system_info()
        print(f"Agent system info: {system_info}")

        await integration.close()

    import asyncio
    asyncio.run(example_usage())