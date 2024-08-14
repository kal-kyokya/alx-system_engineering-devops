#!/usr/bin/python3
"""
API Advanced
"""

import json
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "Mozilla/5.0"}
    print(url)
    response = requests.get(url, headers=headers, allow_redirects=False)
    print(response)
    if response.status_code == 200:
        data = response.json()
        if 'subscribers' in data['data']:
            print(data['data']['subscribers'])
            return data['data']['subscribers']

    return 0
