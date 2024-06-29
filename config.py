import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    FRESHDESK_TOKEN = os.getenv("FRESHDESK_TOKEN")
    GITHUB_API_BASE_URL = os.getenv("GITHUB_API_BASE_URL")
    FRESHDESK_API_BASE_URL = os.getenv("FRESHDESK_API_BASE_URL")
