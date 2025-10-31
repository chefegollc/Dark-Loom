"""Anthropic Claude agent implementation."""

from typing import Any, Optional

from anthropic import AsyncAnthropic

from dark_loom.core.agent import Agent, AgentResponse


class AnthropicAgent(Agent):
    """Agent using Anthropic's Claude models."""

    def __init__(
        self,
        name: str,
        api_key: str,
        model: str = "claude-3-5-sonnet-20241022",
        system_prompt: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize Anthropic agent.

        Args:
            name: Agent name
            api_key: Anthropic API key
            model: Model to use
            system_prompt: System prompt
            **kwargs: Additional arguments
        """
        super().__init__(name=name, system_prompt=system_prompt)
        self.model = model
        self.client = AsyncAnthropic(api_key=api_key)
        self.max_tokens = kwargs.get("max_tokens", 4096)
        self.temperature = kwargs.get("temperature", 0.7)

    async def process(self, message: str, **kwargs: Any) -> AgentResponse:
        """Process a message using Claude.

        Args:
            message: Input message
            **kwargs: Additional arguments

        Returns:
            Agent response
        """
        self.add_message("user", message)

        # Build messages for API
        messages = [{"role": msg.role, "content": msg.content} for msg in self.conversation_history]

        # Call Claude API
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=self.system_prompt,
            messages=messages,
        )

        # Extract response content
        content = ""
        if response.content:
            content = response.content[0].text if hasattr(response.content[0], "text") else str(response.content[0])

        self.add_message("assistant", content)

        return AgentResponse(
            content=content,
            metadata={
                "model": self.model,
                "stop_reason": response.stop_reason,
                "usage": response.usage.model_dump() if response.usage else {},
            },
            finished=response.stop_reason == "end_turn",
        )
