import argparse
from github_api import get_github_user
from freshdesk_api import create_or_update_freshdesk_contact


def main():
    parser = argparse.ArgumentParser(description="GitHub-Freshdesk Integration")
    parser.add_argument(
        "-u", "--username", type=str, required=True, help="GitHub username"
    )
    parser.add_argument(
        "-sd", "--subdomain", type=str, required=True, help="Freshdesk subdomain"
    )
    args = parser.parse_args()

    # Retrieve GitHub user data
    github_user_data = get_github_user(args.username)

    # Create or update Freshdesk contact
    create_or_update_freshdesk_contact(args.subdomain, github_user_data)


if __name__ == "__main__":
    main()
