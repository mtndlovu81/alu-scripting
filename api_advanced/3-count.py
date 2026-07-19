#!/usr/bin/python3
"""Module that recursively counts keyword occurrences in hot article titles."""
import re

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of given keywords in a subreddit's hot articles.

    Prints nothing if the subreddit is invalid or no posts match.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/ariafifty-one)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "")
        for token in re.findall(r"[a-zA-Z']+", title.lower()):
            if token in counts:
                counts[token] += 1

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)

    results = [(word, count) for word, count in counts.items() if count > 0]
    if not results:
        return

    results.sort(key=lambda item: (-item[1], item[0]))
    for word, count in results:
        print(f"{word}: {count}")
