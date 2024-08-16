#!/usr/bin/python3
"""
'redditApp'
"""
import requests
from requests.auth import HTTPBasicAuth


with open('my_reddit_id', 'r') as redID:
    MY_REDDIT_ID = str(redID.read())

with open('secret_k', 'r') as secret:
    SECRET_KEY = str(secret.read())

auth = HTTPBasicAuth(MY_REDDIT_ID, SECRET_KEY)

def number_of_subscribers(subreddit):
    """Fetches the number of subscribers for any given subreddit.
    Argument:
        subreddit: The subreddit to be processed.
    Return:
        The number of subscribers or 0 if error occur.
    """
    if subreddit is None or type(subreddit) != str:
        return 0
    reddit_api = "https://www.reddit.com/r/"
    subreddit_api = reddit_api + subreddit
    url = subreddit_api + "/about.json"
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=header,
                            auth=auth, allow_redirects=False)

    if response.status_code == 200:
        content = response.json()
        if 'subscribers' in content.get('data'):
            return content.get('data').get('subscribers')
    else:
        return 0
