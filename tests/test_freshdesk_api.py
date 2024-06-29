import unittest.mock as mock
from freshdesk_api import get_contact_by_id, update_contact, create_contact


class MockConfig:
    FRESHDESK_TOKEN = "mock_freshdesk_token"
    FRESHDESK_API_BASE_URL = "https://mockfreshdeskdomain.freshdesk.com"


@mock.patch("requests.get")
def test_get_contact_by_id_success(mock_get):
    """Test case for successful retrieval of contact by ID."""
    # Arrange
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [{"id": 1, "unique_external_id": "12345"}]
    mock_get.return_value = mock_response

    # Act
    result = get_contact_by_id(MockConfig.FRESHDESK_API_BASE_URL, "12345")

    # Assert
    assert result == {"id": 1, "unique_external_id": "12345"}
    assert mock_get.return_value.status_code == 200


@mock.patch("requests.get")
def test_get_contact_by_id_failure(mock_get):
    """Test case for failure retrieval of contact by ID."""
    mock_get.side_effect = Exception("Connection Error")

    # Act
    result = get_contact_by_id(MockConfig.FRESHDESK_API_BASE_URL, "12345")

    # Assert
    assert (
        result is None
    )  # Since the function returns None on error, assuming this behavior


@mock.patch("requests.get")
def test_get_contact_by_id_not_found(mock_get):
    """Test case for contact not found scenario."""
    # Arrange
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    # Act
    result = get_contact_by_id(MockConfig.FRESHDESK_API_BASE_URL, "12345")

    # Assert
    assert result is None


@mock.patch("requests.put")
def test_update_contact_success(mock_put):
    """Test case for successful update of contact."""
    # Arrange
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Updated Name"}
    mock_put.return_value = mock_response

    # Act
    result = update_contact(
        MockConfig.FRESHDESK_API_BASE_URL, {"name": "Updated Name"}, "12345"
    )

    # Assert
    assert result == {"id": 1, "name": "Updated Name"}
    assert mock_put.return_value.status_code == 200


@mock.patch("requests.put")
def test_update_contact_failure(mock_put):
    """Test case for failure update of contact."""
    # Arrange
    mock_put.side_effect = Exception("Connection Error")

    # Act
    result = update_contact(
        MockConfig.FRESHDESK_API_BASE_URL, {"name": "Updated Name"}, "12345"
    )

    # Assert
    assert result is None


@mock.patch("requests.post")
def test_create_contact_success(mock_post):
    """Test case for successful creation of contact."""
    # Arrange
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "New Contact"}
    mock_post.return_value = mock_response

    # Act
    result = create_contact(
        MockConfig.FRESHDESK_API_BASE_URL,
        {
            "name": "New Contact",
            "email": "test@example.com",
            "twitter_username": "test_twitter",
            "id": "12345",
        },
    )

    # Assert
    assert result == {"id": 1, "name": "New Contact"}
    assert mock_post.return_value.status_code == 200


@mock.patch("requests.post")
def test_create_contact_failure(mock_post):
    """Test case for failure creation of contact."""
    # Arrange
    mock_post.side_effect = Exception("Connection Error")

    # Act
    result = create_contact(
        MockConfig.FRESHDESK_API_BASE_URL,
        {
            "name": "New Contact",
            "email": "test@example.com",
            "twitter_username": "test_twitter",
            "id": "12345",
        },
    )

    # Assert
    assert result is None
