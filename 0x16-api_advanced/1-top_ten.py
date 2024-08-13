#!/usr/bin/python3
""" top ten posts on reddit"""
import requests


def top_ten(subreddit):
    """Fetch and display the top ten posts from a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "top_posts"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)
