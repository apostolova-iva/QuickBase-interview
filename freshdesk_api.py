import requests
from config import Config


def get_auth_headers():
    """Returns headers with Basic Authentication for Freshdesk API."""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {Config.FRESHDESK_TOKEN}:X",  # Replace 'X' with a password if needed
    }
    return headers


def get_contact_by_id(url_sd, contact_external_id):
    """
    Fetches a contact from Freshdesk by ID.

    Args:
        url_sd (str): The Freshdesk subdomain URL where the contact should be retrieved.
        contact_external_id (str): External ID of the contact to retrieve.

    Returns:
        dict or None: A dictionary containing the contact details if found, else None.
    """
    headers = get_auth_headers()
    try:
        # List all contacts
        response = requests.get(f"{url_sd}/contacts", headers=headers)
        response.raise_for_status()
        contacts = response.json()

        # Find the contact by ID
        for contact in contacts:
            if contact["unique_external_id"] == contact_external_id:
                return contact

        return None  # If no contact found with the given external_id
    except Exception as e:
        print(
            f"An error occurred while trying to fetch a contact from Freshdesk by ID: {e}"
        )


def update_contact(url_sd, mapped_freshdesk_data, freshdesk_contact_id):
    """
    Updates a contact in Freshdesk based on its GitHub account information.

    Args:
        url_sd (str): The Freshdesk subdomain URL where the contact exists.
        mapped_freshdesk_data (dict): Dictionary containing the fields to update for the contact.
        freshdesk_contact_id (str): External ID of the contact.

    Returns:
        dict or None: A dictionary containing the updated contact details if successful, else None.
    """
    headers = get_auth_headers()

    try:
        response = requests.put(
            f"{url_sd}/contacts/{freshdesk_contact_id}",
            json=mapped_freshdesk_data,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"An error occurred while trying to update a contact in Freshdesk: {e}")


def create_contact(url_sd, mapped_freshdesk_data):
    """
    Creates a contact in Freshdesk based on its GitHub account information.

    Args:
        url_sd (str): The Freshdesk subdomain URL where the contact is created.
        mapped_freshdesk_data (dict): Dictionary containing the fields to create the contact.

    Returns:
        dict or None: A dictionary containing the updated contact details if successful, else None.
    """
    headers = get_auth_headers()

    try:
        response = requests.post(
            f"{url_sd}/contacts", json=mapped_freshdesk_data, headers=headers
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"An error occurred while trying to update a contact in Freshdesk: {e}")


def create_or_update_freshdesk_contact(subdomain, user_data):
    """
    Creates a new contact or updates an existing contact in Freshdesk.

    Args:
        subdomain (str): The Freshdesk subdomain where the contact should be created/updated.
        user_data (dict): Dictionary containing GitHub contact information.
    """

    url_sd = Config.FRESHDESK_API_BASE_URL.format(subdomain=subdomain)

    # Map GitHub user fields to Freshdesk contact fields
    mapped_freshdesk_data = {
        "name": user_data["name"],
        "email": user_data["email"],
        "twitter_id": user_data["twitter_username"],
        "unique_external_id": user_data["id"],
    }

    # Fetch a contact from Freshdesk if existing
    existing_contact = get_contact_by_id(
        url_sd, mapped_freshdesk_data["unique_external_id"]
    )

    if existing_contact:
        # Update existing contact
        contact_id = existing_contact["id"]
        update_contact(url_sd, mapped_freshdesk_data, contact_id)
    else:
        # Create new contact
        create_contact(url_sd, mapped_freshdesk_data)
