#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
to print the titles of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid, prints None.

    :param subreddit: the name of the subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python/requests: API project by /u/yourusername'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data', {}).get('children', [])
                for post in posts:
                    print(post.get('data', {}).get('title'))
            except ValueError:
                print("Error: Unable to parse JSON response.")
        else:
            print(None)
    except requests.RequestException as e:
        print(f"Error: {e}")
        print(None)
