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
    if resp.status_code != 200 or after is None:
        print('None')
        return
    else:
        json_resp = resp.json()
        data_posts = resp.json()['data']['children']
        if i == len(data_posts):
            return (len(data_posts))
        else:
            hot_list.append(data_posts[i]['data']['title'])
            recurse(subreddit, hot_list, after, i + 1)
        after = resp.json()['data']['after']
        print(after)
        recurse(subreddit, hot_list, after)
    return (hot_list)
