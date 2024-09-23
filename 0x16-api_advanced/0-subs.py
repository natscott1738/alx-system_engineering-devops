#!/usr/bin/python3
"""Defines number of subs"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit.
    If subreddit is invalid, returns 0.
    """
    # Set a custom User-Agent to avoid "Too Many Requests" errors
    headers = {'User-Agent': 'myRedditAPIClient/0.1'}

    # Define the URL for Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract the number of subscribers
            return data.get('data', {}).get('subscribers', 0)
        elif response.status_code == 302:
            # If we get a redirect, it indicates an invalid subreddit
            return 0
        else:
            # For any other HTTP errors, assume invalid subreddit
            return 0
    except requests.RequestException:
        # Handle any exceptions that occur during the request
        return 0
