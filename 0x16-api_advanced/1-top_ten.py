#!/usr/bin/python3
"""
'1-top_ten' Creates a function that manipulates the Reddit API.
"""
from redditAuth import auth
import requests


def top_ten(subreddit):
    """Fetches the 10 most popular posts of a subreddit

    Arg:
       subreddit: The subreddit to be processed

    Return:
        None if the subreddit is invalid
    """
    if subreddit is None or type(subreddit) != str:
        return None
    reddit_api = "https://www.reddit.com/r/"
    subreddit_api = reddit_api + subreddit
    url = subreddit_api + "/top.json?limit=10"
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=header,
                            auth=auth, allow_redirects=False)

    if response.status_code == 200:
        content = response.json()
        posts_list = content.get('data').get('children')
        for post in posts_list:
            title = post.get('data').get('title')
            print(title)
    else:
        return None
