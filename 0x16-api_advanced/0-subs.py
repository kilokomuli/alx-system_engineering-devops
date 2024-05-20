#!/usr/bin/python3
""" A function that queries the Reddit API and returns the number of
subscribers"""
import requests


def number_of_subscribers(subreddit):
    """REturns total number of subscribers on a given reddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "custom-user-agent"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
