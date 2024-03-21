""" Fetching all organizations from GitHub """
import os
import requests
# Retrieving GitHub access token from environment variable
token = os.environ.get("GITHUB_ACCESS_TOKEN")
if not token:
    print("GitHub access token not found. Please set GITHUB_ACCESS_TOKEN environment variable.")

def get_all_organizations():
    """
    This function retrieves names of all organizations from GitHub.

    Returns:
        list: Names of all organizations.
    """
    url_org = "https://api.github.com/user/orgs"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url_org, headers=headers)

    if response.status_code == 200:
        organizations = response.json()
        orgs_name = [org.get("login") for org in organizations]
        return orgs_name
    else:
        print("Failed to retrieve organizations. Status code:", response.status_code)
        return None

# Calling the function to get organization names
organization_names = get_all_organizations()

# Displaying organization names if found, otherwise printing a message
if organization_names:
    print("GitHub Organization Names : ")
    for org_name in organization_names:
        print(org_name)
else:
    print("No organizations found.")
