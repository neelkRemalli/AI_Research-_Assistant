from research_assistant.llm_client import LLMClient
from research_assistant.retriever import search_information


def research(
    question: str,
    client: LLMClient,
    model: str,
) -> str:
    information = search_information(question)

    if not information:
        raise ValueError("No information found.")

    system_prompt = """
You are a research assistant.

Answer the user's question using only the
provided information.

If the information does not contain enough
evidence to answer the question, say so.
"""

    user_prompt = f"""
Question:
{question}

Retrieved information:
{information}
"""

    return client.generate(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        model=model,
        temperature=0.2,
    )


