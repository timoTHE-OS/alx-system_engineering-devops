#!/usr/bin/python3
"""returns the number of subscribers for a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers or 0"""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    url_r = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url=url_r)
    data = response.json()
    print(data)
    try:
        return data['data']['subscribers']
    except Exception:
        return 0
