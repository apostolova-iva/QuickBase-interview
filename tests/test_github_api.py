from unittest import mock
from github_api import get_github_user


class MockConfig:
    GITHUB_TOKEN = "mock_token"
    GITHUB_API_BASE_URL = "https://api.github.com"


@mock.patch("requests.get")
def test_get_github_user_success(mock_get):
    """Test case for successful retrieval of user by username."""
    # Arrange
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"login": "test_user", "name": "Test User"}
    mock_get.return_value = mock_response

    # Act
    result = get_github_user("test_user")

    # Assert
    assert result == {"login": "test_user", "name": "Test User"}
    assert mock_get.return_value.status_code == 200


@mock.patch("requests.get")
def test_get_github_user_exception(mock_get):
    """Test case for failure retrieval of user by username."""
    # Arrange
    mock_get.side_effect = Exception("Connection Error")

    # Act
    result = get_github_user("test_user")

    # Assert
    assert (
        result is None
    )  # Since the function returns None on error, assuming this behavior
