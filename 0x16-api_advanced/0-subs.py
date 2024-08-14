#!/usr/bin/python3
"""
Query subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Alogyn)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 403:
        return Ok
    results = response.json().get("data")
    return results.get("subscribers")
