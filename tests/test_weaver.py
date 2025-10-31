"""Tests for weaver module."""

import pytest

from dark_loom.core.agent import Agent, AgentResponse
from dark_loom.core.weaver import Weaver, WeaverTask


class MockAgent(Agent):
    """Mock agent for testing."""

    async def process(self, message: str, **kwargs) -> AgentResponse:  # type: ignore[misc]
        """Mock process method."""
        return AgentResponse(content=f"Processed: {message}", finished=True)


def test_weaver_initialization() -> None:
    """Test weaver initialization."""
    weaver = Weaver()
    assert len(weaver.agents) == 0
    assert len(weaver.tasks) == 0


def test_weaver_register_agent() -> None:
    """Test registering an agent."""
    weaver = Weaver()
    agent = MockAgent(name="TestAgent")
    weaver.register_agent(agent)
    assert "TestAgent" in weaver.agents
    assert weaver.agents["TestAgent"] == agent


def test_weaver_unregister_agent() -> None:
    """Test unregistering an agent."""
    weaver = Weaver()
    agent = MockAgent(name="TestAgent")
    weaver.register_agent(agent)
    weaver.unregister_agent("TestAgent")
    assert "TestAgent" not in weaver.agents


def test_weaver_add_task() -> None:
    """Test adding a task."""
    weaver = Weaver()
    task = WeaverTask(task_id="task1", description="Test task")
    weaver.add_task(task)
    assert "task1" in weaver.tasks
    assert weaver.tasks["task1"] == task


def test_weaver_list_agents() -> None:
    """Test listing agents."""
    weaver = Weaver()
    agent1 = MockAgent(name="Agent1")
    agent2 = MockAgent(name="Agent2")
    weaver.register_agent(agent1)
    weaver.register_agent(agent2)
    agents = weaver.list_agents()
    assert len(agents) == 2
    assert "Agent1" in agents
    assert "Agent2" in agents


async def test_weaver_execute_task() -> None:
    """Test executing a task."""
    weaver = Weaver()
    agent = MockAgent(name="TestAgent")
    weaver.register_agent(agent)

    task = WeaverTask(task_id="task1", description="Test task", agent="TestAgent")
    weaver.add_task(task)

    result = await weaver.execute_task("task1")
    assert result is not None
    assert task.status == "completed"


async def test_weaver_execute_nonexistent_task() -> None:
    """Test executing a nonexistent task."""
    weaver = Weaver()
    with pytest.raises(ValueError, match="Task .* not found"):
        await weaver.execute_task("nonexistent")
