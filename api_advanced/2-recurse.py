#!/usr/bin/python3
"""Module that recursively queries the Reddit API for hot article titles.

This module contains a single function, recurse, which returns a list
of titles of all hot articles for a given subreddit by paginating
through the Reddit API results recursively.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles for a given subreddit.

    If the subreddit is invalid, return None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ariafifty-one)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
