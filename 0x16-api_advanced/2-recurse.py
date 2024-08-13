#!/usr/bin/python3
"""recursive hot posts of reddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """recursive hot posts of reddit"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        after = data['data']['after']
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
