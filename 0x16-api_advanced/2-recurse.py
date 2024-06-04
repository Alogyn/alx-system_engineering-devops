#!/usr/bin/python3
"""
Contains the recurse function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API and returns a list of titles of all hot posts
    for a given subreddit. If the subreddit is invalid, returns None.

    :param subreddit: the name of the subreddit
    :param hot_list: list to accumulate hot post titles
    :param after: the next page token for pagination
    :return: list of hot post titles or None if invalid subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    try:
        results = response.json().get("data")
    except ValueError:
        return None

    after = results.get("after")
    children = results.get("children", [])
    for child in children:
        hot_list.append(child.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
