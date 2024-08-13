#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit"""
import requests

headers = {"User-Agent": "MyCustomUserAgent/1.0"}


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    request = requests.get(
        url,
        headers={"User-Agent": "Custom"},
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
