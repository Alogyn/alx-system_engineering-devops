#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to get the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.

    :param subreddit: the name of the subreddit
    :return: the number of subscribers or 0 if invalid subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/requests: API project by /u/yourusername'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except requests.RequestException:
        return 0
