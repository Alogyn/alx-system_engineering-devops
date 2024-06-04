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
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "0x16-api_advanced:project: \
                v1.0.0 (by /u/firdaus_cartoon_jr)"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get("data")
        children = data.get("children")
    except ValueError:
        print(None)
        return

    if children:
        for child in children:
            title = child.get("data").get("title")
            print(title)
    else:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
