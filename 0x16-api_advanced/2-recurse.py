#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """return top 10 posts of subreddit"""
    url = "https://www.reddit.com/r/{}.json".format(subreddit)
    if after:
        url = "https://www.reddit.com/r/{}.json?\
               after={}".format(subreddit, after)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "Ubuntu"}
    h.update(headers)
    r = requests.get(url, headers=h, allow_redirects=False).json()
    if not r:
        return None
    posts = r.get('data', {}).get('children', [])
    for post in posts:
        hot_list.append(post['data']['title'])
    after = r.get('data').get('after')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
