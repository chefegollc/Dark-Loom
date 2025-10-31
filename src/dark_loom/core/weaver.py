"""Weaver - orchestration engine for Dark-Loom."""

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from dark_loom.core.agent import Agent, AgentResponse


class WeaverTask(BaseModel):
    """A task to be executed by the Weaver."""

    task_id: str = Field(..., description="Unique task identifier")
    description: str = Field(..., description="Task description")
    agent: Optional[str] = Field(default=None, description="Agent to use for task")
    dependencies: List[str] = Field(default_factory=list, description="Task dependencies")
    status: str = Field(default="pending", description="Task status")
    result: Optional[Any] = Field(default=None, description="Task result")


class Weaver:
    """Orchestration engine for coordinating multiple agents."""

    def __init__(self, config: Optional[Any] = None) -> None:
        """Initialize the Weaver.

        Args:
            config: Configuration object
        """
        self.config = config
        self.agents: Dict[str, Agent] = {}
        self.tasks: Dict[str, WeaverTask] = {}

    def register_agent(self, agent: Agent) -> None:
        """Register an agent with the Weaver.

        Args:
            agent: Agent to register
        """
        self.agents[agent.name] = agent

    def unregister_agent(self, agent_name: str) -> None:
        """Unregister an agent.

        Args:
            agent_name: Name of agent to unregister
        """
        if agent_name in self.agents:
            del self.agents[agent_name]

    def add_task(self, task: WeaverTask) -> None:
        """Add a task to the weaver.

        Args:
            task: Task to add
        """
        self.tasks[task.task_id] = task

    async def execute_task(self, task_id: str, context: Optional[Dict[str, Any]] = None) -> Any:
        """Execute a single task.

        Args:
            task_id: ID of task to execute
            context: Optional context for execution

        Returns:
            Task result

        Raises:
            ValueError: If task not found or agent not available
        """
        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} not found")

        task = self.tasks[task_id]

        # Check dependencies
        for dep_id in task.dependencies:
            if dep_id in self.tasks:
                dep_task = self.tasks[dep_id]
                if dep_task.status != "completed":
                    raise ValueError(f"Dependency {dep_id} not completed")

        # Execute task
        if task.agent:
            if task.agent not in self.agents:
                raise ValueError(f"Agent {task.agent} not found")

            agent = self.agents[task.agent]
            task.status = "running"

            response = await agent.process(task.description, context=context)
            task.result = response
            task.status = "completed"

            return response
        else:
            # Task without specific agent
            task.status = "completed"
            return None

    async def weave(
        self, goal: str, agents: Optional[List[Agent]] = None, max_iterations: int = 10
    ) -> List[AgentResponse]:
        """Execute a complex goal using multiple agents.

        Args:
            goal: High-level goal to achieve
            agents: Optional list of agents to use
            max_iterations: Maximum iterations

        Returns:
            List of agent responses
        """
        if agents:
            for agent in agents:
                self.register_agent(agent)

        responses: List[AgentResponse] = []

        # Simple orchestration loop
        for i in range(max_iterations):
            # In a real implementation, this would use a more sophisticated
            # planning and execution strategy
            if not self.agents:
                break

            # For now, just use the first agent
            agent = list(self.agents.values())[0]
            response = await agent.process(goal)
            responses.append(response)

            if response.finished:
                break

        return responses

    def get_task_status(self, task_id: str) -> Optional[str]:
        """Get status of a task.

        Args:
            task_id: Task ID

        Returns:
            Task status or None if not found
        """
        task = self.tasks.get(task_id)
        return task.status if task else None

    def list_agents(self) -> List[str]:
        """List registered agents."""
        return list(self.agents.keys())

    def list_tasks(self) -> List[WeaverTask]:
        """List all tasks."""
        return list(self.tasks.values())
