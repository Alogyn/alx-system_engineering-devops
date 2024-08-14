#!/usr/bin/python3
"""
Query subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'MyRedditApp/1.0 (by /u/Alogyn)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 403:
            print("403 Forbidden: Access is denied.")
            return 0
        elif response.status_code != 200:
            print(f"Unexpected Status Code: {response.status_code}")
            return 0

        data = response.json().get('data', {})
        return data.get('subscribers', 0)
    except Exception as e:
        print(f"Error: {e}")
        return 0
