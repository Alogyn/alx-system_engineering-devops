#!/usr/bin/python3
"""
Contains the top_ten function
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    :param subreddit: the name of the subreddit
    """
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'reddit-top-ten'}

    # Form the URL for the subreddit's hot posts with a limit of 10
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        else:
            # If not 200, print None (either invalid subreddit or some other error)
            print(None)
    except Exception:
        # In case of any request errors, print None
        print(None)

