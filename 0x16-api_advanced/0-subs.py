#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
