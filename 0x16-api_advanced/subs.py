#!/usr/bin/python3
"""Script for parsing web data from an API"""
import json
import requests
import sys

def number_of_subscribers(subreddit):
    """API call to Reddit to get the number of subscribers"""
    base_url = 'https://www.reddit.com/r/'
    headers = {
        'User-Agent': 'MyRedditApp/0.1 by YourRedditUsername'
    }
    url = f"{base_url}{subreddit}/about.json"
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 403:
            print("Error: Access forbidden.", end="")
            print("Check if the subreddit exists or if authentication is required.")
            return 0
        elif response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return 0

        try:
            resp = response.json()
        except json.JSONDecodeError:
            print("Error: Couldn't parse JSON")
            return 0

        data = resp.get('data')
        if not data:
            return 0

        subscribers = data.get('subscribers')
        return int(subscribers) if subscribers else 0

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./main.py <subreddit>")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
