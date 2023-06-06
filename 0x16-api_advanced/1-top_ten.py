#!/usr/bin/python3
""" function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """return top 10 posts of subreddit"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "Ubuntu"}
    h.update(headers)
    r = requests.get(url, headers=h, allow_redirects=False).json()
    if not r:
        return None
    else:
        posts = r.get('data', {}).get('children', [])
        for i in range(0, 10):
            print(posts[i]['data']['title'])
