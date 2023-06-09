#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """return top 10 posts of subreddit"""
    url = "https://www.reddit.com/r/{}.json?\
           after={}".format(subreddit, after)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "Ubuntu"}
    h.update(headers)
    r = requests.get(url, headers=h)
    if r.status_code != 200:
        return None
    data = r.json().get('data')
    if not data:
        return hot_list
    posts = data.get('children')
    for post in posts:
        hot_list.append(post['data']['title'])
    after = data.get('after')
    if after is not None:
        recurse(subreddit, hot_list, after)
    return hot_list
