#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    :param subreddit: the name of the subreddit
    :return: number of subscribers (int), or 0 if the subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project: \
                v1.0.0 (by /u/firdaus_cartoon_jr)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except ValueError:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(sys.argv[1]))
