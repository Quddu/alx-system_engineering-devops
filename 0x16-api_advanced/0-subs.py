#!/usr/bin/python3
'''
    this module contains the function number_of_subscribers
'''
import requests
import sys

def number_of_subscribers(subreddit):
    '''
        returns the number of subscribers for a given subreddit
    '''
    user_agent = 'Lizzie'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    try:
        data = response.json()['data']
        return data['subscribers']
    except KeyError:
        return 0

if __name__ == "__main__":
    subreddit = sys.argv[1]
    print(number_of_subscribers(subreddit))
