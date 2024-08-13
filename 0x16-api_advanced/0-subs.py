#!/usr/bin/python3
""" function return num of subsecribers"""
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
