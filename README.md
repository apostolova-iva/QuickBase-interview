# GitHub to Freshdesk Integration

## Description

This command line Python program retrieves information about a GitHub user and creates a new contact or updates an existing contact in Freshdesk using their respective APIs.

## Requirements

- Python 3.x
- `python-dotenv` library
- `requests` library

## Installation

1. **Clone the repository:**

2. **Install the required libraries:**

    ```
    pip install -r requirements.txt
    ```

3. **Create a `.env` file based on the provided `.env.example` and fill in your tokens and URLs:**

    Duplicate the `.env.example` file:

    ```
    cp .env.example .env
    ```

    Edit the `.env` file to include your GitHub token and Freshdesk token:

    ```
    FRESHDESK_API_BASE_URL=https://{subdomain}.freshdesk.com/api/v2
    GITHUB_API_BASE_URL=https://api.github.com
    sGITHUB_TOKEN=your_github_token
    FRESHDESK_TOKEN=your_freshdesk_token
    ```

## Usage

To use the program, run `main.py` with the GitHub username and Freshdesk subdomain parameters:

```
python main.py -u <github_username> -sd <freshdesk_subdomain>
```

## Project Structure

The project directory is structured as follows:

```
./
├── config.py
├── freshdesk_api.py
├── github_api.py
├── main.py
├── tests/
│   ├── test_freshdesk_api.py
│   └── test_github_api.py
├── requirements.txt
└── .env.example
```

## Running Tests

Run the unit tests using pytest:

```
pytest test_github_api.py
pytest test_freshdesk_api.py
```

## Files Description

Here's a brief description of each file in the project directory:

- **`config.py`**: This file handles the configuration settings for the project. It loads environment variables from the `.env` file using `python-dotenv`.

- **`freshdesk_api.py`**: Contains functions that interact with the Freshdesk API. This includes creating new contacts and updating existing ones based on GitHub user data.

- **`github_api.py`**: Provides functions to interact with the GitHub API. It retrieves information about a GitHub user using the GitHub REST API v3.

- **`main.py`**: This is the main entry point of the program. It accepts command-line arguments for GitHub username (`-u` or `--username`) and Freshdesk subdomain (`-sd` or `--subdomain`). It orchestrates the integration between GitHub and Freshdesk by fetching GitHub user data and creating or updating Freshdesk contacts accordingly.

- **`tests/` Directory**:
  - **`test_freshdesk_api.py`**: Contains unit tests for functions defined in `freshdesk_api.py`. It mocks API responses and tests different scenarios related to creating and updating Freshdesk contacts.

  - **`test_github_api.py`**: Includes unit tests for functions defined in `github_api.py`. It mocks API responses and verifies the behavior of functions that interact with the GitHub API.

- **`requirements.txt`**: Lists all Python libraries required for the project. These dependencies can be installed using `pip install -r requirements.txt`.

- **`.env.example`**: Provides an example structure for setting up environment variables required by the project (`FRESHDESK_API_BASE_URL`, `GITHUB_API_BASE_URL`, `GITHUB_TOKEN`, `FRESHDESK_TOKEN`). Before running the program, duplicate this file as `.env` and fill in your specific tokens and URLs.
