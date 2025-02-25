#!/usr/bin/python3
""" Queries the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """ Return total subscribers on a given subreddit """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json.get("data")
    return results.get("subscribers")
