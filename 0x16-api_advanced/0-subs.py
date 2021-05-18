#!/usr/bin/python3
"""Function to query"""
import requests


def number_of_subscribers(subreddit):
    """ Return the number of subscribers
        (not active users, total subscribers)
        with Reddit API. Set a custom-Agent if needed.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
                       (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    url = "https://www.reddit.com/r/{}/about.json"
    resp = requests.get(url.format(subreddit), headers=headers)
    if resp.status_code != 200:
        return (0)
    else:
        json_resp = resp.json()['data']
        # json_resp = json.dumps(json_resp, indent=4, sort_keys=True)
        # print(json_resp) or firefox
        subscribers = (json_resp.get('subscribers'))
    return (subscribers)
