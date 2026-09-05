from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    BadRequestError,
)

from research_assistant.config import get_api_key
from research_assistant.llm_client import LLMClient
from research_assistant.research import research


def main() -> None:
    try:
        api_key = get_api_key()

        client = LLMClient(api_key)

        question = input("Enter your research question: ").strip()

        if not question:
            raise ValueError("Question cannot be empty.")

        model = input("Enter model: ").strip()

        if not model:
            raise ValueError("Model cannot be empty.")

        result = research(
            question=question,
            client=client,
            model=model,
        )

        print("\nResearch result:")
        print(result)

    except ValueError as error:
        print(f"Input/configuration error: {error}")

    except AuthenticationError:
        print("Authentication failed. Check your API key.")

    except BadRequestError as error:
        print(f"Bad request: {error}")

    except APIConnectionError:
        print("Could not connect to the OpenAI API.")

    except APIStatusError as error:
        print(f"API error: {error.status_code}")


if __name__ == "__main__":
    main()