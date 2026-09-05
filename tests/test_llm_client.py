from unittest.mock import Mock

from research_assistant.llm_client import LLMClient


def test_generate():
    client = LLMClient("fake-api-key")

    mock_response = Mock()
    mock_response.output_text = "Python is a programming language."

    client.client.responses.create = Mock(
        return_value=mock_response
    )

    result = client.generate(
        system_prompt="You are helpful.",
        user_prompt="What is Python?",
        model="gpt-5",
    )

    assert result == "Python is a programming language."

    client.client.responses.create.assert_called_once_with(
        model="gpt-5",
        instructions="You are helpful.",
        input="What is Python?",
        temperature=1.0,
    )