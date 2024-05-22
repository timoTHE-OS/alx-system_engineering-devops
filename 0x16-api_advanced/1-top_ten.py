#!/usr/bin/python3
"""queries the Reddit API """
import requests


def top_ten(subreddit):
    """prints the top ten hot post"""
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
        print('None')
