#!/usr/bin/python3
'''
    this module contains the function top_ten
'''
import requests
import sys

def top_ten(subreddit):
    '''
        returns the top ten posts for a given subreddit
    '''
    user_agent = 'Lizzie'
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    try:
        data = response.json()['data']
        for post in data['children']:
            print(post['data']['title'])
    except Exception:
        print(None)

if __name__ == "__main__":
    subreddit = sys.argv[1]
    top_ten(subreddit)
