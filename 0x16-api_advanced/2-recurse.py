#!/usr/bin/python3
"""Function to query"""
import requests


def recurse(subreddit, hot_list=[], after='', i=0):
    """ Return the top ten hot title of reddit.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
                       (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    url = "https://www.reddit.com/r/{}/hot.json?after={}"
    resp = requests.get(url.format(subreddit, after), headers=headers,
                        allow_redirects=False)
    if resp.status_code != 200:
        return None
    elif after is None:
        return
    else:
        json_resp = resp.json()
        data_posts = resp.json()['data']['children']
        for data in data_posts:
            title = data['data']['title']
            hot_list.append(title)
        after = resp.json()['data']['after']
        recurse(subreddit, hot_list, after)
    return (hot_list)
