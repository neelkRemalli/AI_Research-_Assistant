from unittest.mock import Mock, patch

from research_assistant.research import research


@patch("research_assistant.research.search_information")
def test_research(mock_search):
    mock_search.return_value = (
        "Python is a high-level programming language."
    )

    client = Mock()

    client.generate.return_value = (
        "Python is a high-level programming language."
    )

    result = research(
        question="What is Python?",
        client=client,
        model="gpt-5",
    )

    assert result == (
        "Python is a high-level programming language."
    )

    mock_search.assert_called_once_with("What is Python?")

    client.generate.assert_called_once()