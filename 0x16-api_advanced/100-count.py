#!/usr/bin/python3
"""
Contains the count_words function
"""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the Reddit API and counts the occurrences of keywords in the
    titles of all hot posts. Prints the counts sorted by count (descending)
    and then alphabetically (ascending).

    :param subreddit: the name of the subreddit
    :param word_list: list of keywords to count
    :param after: the next page token for pagination
    :param counts: dictionary to accumulate counts of keywords
    """
    if counts is None:
        # Initialize counts dictionary with lowercase keywords
        counts = {word.lower(): 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project: \
                v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "limit": 100
    }

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code == 404:
        return

    try:
        results = response.json().get("data")
    except ValueError:
        return

    after = results.get("after")
    children = results.get("children", [])

    for child in children:
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            counts[word.lower()] += title.count(word.lower())

    if after is not None:
        count_words(subreddit, word_list, after, counts)
    else:
        # Sorting the counts dictionary by value (descending) and then by
        # key (ascending)
        sorted_counts = sorted(
            counts.items(), key=lambda item: (-item[1], item[0])
        )
        for word, count in sorted_counts:
            if count > 0:
                print(f"{word}: {count}")
