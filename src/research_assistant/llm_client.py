from openai import OpenAI


class LLMClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(
            api_key=api_key,
        )

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        model: str,
        temperature: float = 1.0,
    ) -> str:
        response = self.client.responses.create(
            model=model,
            instructions=system_prompt,
            input=user_prompt,
            temperature=temperature,
        )

        return response.output_text


