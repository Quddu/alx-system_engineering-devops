#!/usr/bin/python3
"""Contains recurse function"""
import requests

def recurse(subreddit, hot_list=None, after=None, count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code != 200:
        return None
    
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))
    
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list
