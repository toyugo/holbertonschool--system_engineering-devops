#!/usr/bin/python3
"""Function to query"""
import requests


def top_ten(subreddit):
    """ Return the top ten hot title of reddit.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
                       (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    url = "https://www.reddit.com/r/{}/hot.json?limit=10"
    resp = requests.get(url.format(subreddit), headers=headers,
                        allow_redirects=False)
    if resp.status_code != 200:
        print('None')
        return
    else:
        json_resp = resp.json()
        data_posts = resp.json()['data']['children']
        for data in data_posts:
            title = data['data']['title']
            print(title)
    return
