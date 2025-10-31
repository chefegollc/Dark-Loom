"""OpenAI agent implementation."""

from typing import Any, Optional

from openai import AsyncOpenAI

from dark_loom.core.agent import Agent, AgentResponse


class OpenAIAgent(Agent):
    """Agent using OpenAI's models."""

    def __init__(
        self,
        name: str,
        api_key: str,
        model: str = "gpt-4",
        system_prompt: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize OpenAI agent.

        Args:
            name: Agent name
            api_key: OpenAI API key
            model: Model to use
            system_prompt: System prompt
            **kwargs: Additional arguments
        """
        super().__init__(name=name, system_prompt=system_prompt)
        self.model = model
        self.client = AsyncOpenAI(api_key=api_key)
        self.max_tokens = kwargs.get("max_tokens", 4096)
        self.temperature = kwargs.get("temperature", 0.7)

    async def process(self, message: str, **kwargs: Any) -> AgentResponse:
        """Process a message using OpenAI.

        Args:
            message: Input message
            **kwargs: Additional arguments

        Returns:
            Agent response
        """
        self.add_message("user", message)

        # Build messages for API
        messages = [
            {"role": "system", "content": self.system_prompt},
            *[{"role": msg.role, "content": msg.content} for msg in self.conversation_history],
        ]

        # Call OpenAI API
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
        )

        # Extract response content
        content = response.choices[0].message.content or ""
        finish_reason = response.choices[0].finish_reason

        self.add_message("assistant", content)

        return AgentResponse(
            content=content,
            metadata={
                "model": self.model,
                "finish_reason": finish_reason,
                "usage": response.usage.model_dump() if response.usage else {},
            },
            finished=finish_reason == "stop",
        )
