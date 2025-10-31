"""Tests for agent module."""

from dark_loom.core.agent import Agent, AgentResponse, Message


class MockAgent(Agent):
    """Mock agent for testing."""

    async def process(self, message: str, **kwargs) -> AgentResponse:  # type: ignore[misc]
        """Mock process method."""
        return AgentResponse(content=f"Echo: {message}", finished=True)


def test_agent_initialization() -> None:
    """Test agent initialization."""
    agent = MockAgent(name="TestAgent")
    assert agent.name == "TestAgent"
    assert len(agent.conversation_history) == 0


def test_agent_add_message() -> None:
    """Test adding messages to conversation history."""
    agent = MockAgent(name="TestAgent")
    agent.add_message("user", "Hello")
    assert len(agent.conversation_history) == 1
    assert agent.conversation_history[0].role == "user"
    assert agent.conversation_history[0].content == "Hello"


def test_agent_clear_history() -> None:
    """Test clearing conversation history."""
    agent = MockAgent(name="TestAgent")
    agent.add_message("user", "Hello")
    agent.clear_history()
    assert len(agent.conversation_history) == 0


async def test_agent_process() -> None:
    """Test agent process method."""
    agent = MockAgent(name="TestAgent")
    response = await agent.process("Test message")
    assert response.content == "Echo: Test message"
    assert response.finished is True
