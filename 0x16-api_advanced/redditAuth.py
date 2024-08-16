#!/usr/bin/python3
"""
'redditAuth' avails Authentication data for Reddit API calls
"""
from requests.auth import HTTPBasicAuth


with open('my_reddit_id', 'r') as redID:
    MY_REDDIT_ID = str(redID.read())

with open('secret_k', 'r') as secret:
    SECRET_KEY = str(secret.read())

auth = HTTPBasicAuth(MY_REDDIT_ID, SECRET_KEY)
