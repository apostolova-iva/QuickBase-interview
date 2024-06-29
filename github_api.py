import requests
from config import Config


def get_github_headers():
    """Returns headers for GitHub API."""
    headers = {
        "Authorization": Config.GITHUB_TOKEN,
        "Accept": "application/vnd.github.v3+json",
    }
    return headers


def get_github_user(username):
    """
    Fetches information about a GitHub user using the GitHub REST API v3.

    Args:
        username (str): The GitHub username of the user whose information is to be retrieved.

    Returns:
        dict: A dictionary containing information about the GitHub user, parsed from JSON response.
    """
    headers = get_github_headers()

    try:
        response = requests.get(
            f"{Config.GITHUB_API_BASE_URL}/users/{username}", headers=headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(
            f"An error occurred while trying to fetch information about a GitHub user: {e}"
        )
