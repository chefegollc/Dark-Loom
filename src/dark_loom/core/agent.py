"""Agent implementation for Dark-Loom."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Message(BaseModel):
    """A message in the conversation."""

    role: str = Field(..., description="Role of the message sender")
    content: str = Field(..., description="Content of the message")
    metadata: Dict[str, Any] = Field(default_factory=dict)


class AgentResponse(BaseModel):
    """Response from an agent."""

    content: str = Field(..., description="Response content")
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tool_calls: List[Dict[str, Any]] = Field(default_factory=list)
    finished: bool = Field(default=True)


class Agent(ABC):
    """Abstract base class for AI agents."""

    def __init__(
        self,
        name: str,
        system_prompt: Optional[str] = None,
        tools: Optional[List[Any]] = None,
    ) -> None:
        """Initialize the agent.

        Args:
            name: Name of the agent
            system_prompt: System prompt for the agent
            tools: List of tools available to the agent
        """
        self.name = name
        self.system_prompt = system_prompt or self._default_system_prompt()
        self.tools = tools or []
        self.conversation_history: List[Message] = []

    def _default_system_prompt(self) -> str:
        """Get default system prompt."""
        return f"You are {self.name}, an AI agent in the Dark-Loom framework."

    @abstractmethod
    async def process(self, message: str, **kwargs: Any) -> AgentResponse:
        """Process a message and return a response.

        Args:
            message: Input message to process
            **kwargs: Additional arguments

        Returns:
            Agent response
        """
        pass

    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Add a message to conversation history.

        Args:
            role: Role of the message sender
            content: Content of the message
            metadata: Optional metadata
        """
        self.conversation_history.append(
            Message(role=role, content=content, metadata=metadata or {})
        )

    def clear_history(self) -> None:
        """Clear conversation history."""
        self.conversation_history.clear()

    def get_history(self) -> List[Message]:
        """Get conversation history."""
        return self.conversation_history.copy()
