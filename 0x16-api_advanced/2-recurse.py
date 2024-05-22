#!/usr/bin/python3
"""queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[]):
    """uses recursion to print post"""
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
    url_r = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url=url_r)
    data = response.json()
    try:
        posts = data['data']['children']
        for i in range(0, 10):
            print(posts[i])
    except Exception:
        return None
