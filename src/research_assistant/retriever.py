import requests


def search_information(query: str) -> str:
    # response = requests.get(
    #     "https://en.wikipedia.org/w/api.php",
    #     params={
    #         "action": "query",
    #         "list": "search",
    #         "srsearch": query,
    #         "format": "json",
    #     },
    #     timeout=10,
    # )
    response = requests.get(
    "https://en.wikipedia.org/w/api.php",
    params={
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
    },
    headers={
        "User-Agent": "AI-Research-Assistant/1.0"
    },
    timeout=10,
)

    response.raise_for_status()

    data = response.json()

    results = data.get("query", {}).get("search", [])

    if not results:
        return ""

    return results[0].get("snippet", "")