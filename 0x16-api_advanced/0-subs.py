#!/usr/bin/python3
"""function that queries the Reddit API and returns
the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return total subscribers of a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = requests.utils.default_headers()
    headers = {'User-Agent': "Ubuntu"}
    h.update(headers)
    r = requests.get(url, headers=h, allow_redirects=False).json()
    count = r.get('data', {}).get('subscribers')
    if not count:
        return 0
    else:
        return count
