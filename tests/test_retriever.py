from unittest.mock import Mock, patch

from research_assistant.retriever import search_information


@patch("research_assistant.retriever.requests.get")
def test_search_information(mock_get):
    mock_response = Mock()

    mock_response.json.return_value = {
        "query": {
            "search": [
                {
                    "snippet": "Python is a programming language."
                }
            ]
        }
    }

    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = search_information("Python")

    assert result == "Python is a programming language."

    mock_get.assert_called_once()