#!/usr/bin/python3
"""Return the number of subscribers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    If the subreddit is invalid, return 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ariafifty-one)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        return response.json().get("data", {}).get("subscribers", 0)
    except ValueError:
        return 0
