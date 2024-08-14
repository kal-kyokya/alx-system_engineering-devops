#!/usr/bin/python3
"""
'0-subs' define a function that manipulate the 'Reddit API'
"""
import requests


def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for any given subreddit.

    Arg:
        subreddit: The subreddit to be processed.

    Return:
        The number of subscribers or 0 if error occur.
    """
    reddit_api = "https://www.reddit.com/r/"
    subreddit_api = reddit_api + subreddit
    url = subreddit_api + "/about.json"
    header = {"User-Agent": "Mozilla/5.0"}
    print(url)
    response = requests.get(url, headers=header).json()
    print(response.status_code)

    if response:
        return response.get("subscribers")
    else:
        return 0
