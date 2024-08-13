#!/usr/bin/python3
"""
Query subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    headers = {'User-Agent': 'reddit-subscriber-counter'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
