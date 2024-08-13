#!/usr/bin/python3
""" function return num of subsecribers"""
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
