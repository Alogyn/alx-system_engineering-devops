#!/usr/bin/python3
"""
Query subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyRedditApp/1.0 (by /u/Alogyn; contact: derfoufi.mohamed96@gmail.com)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception:
        return 0
