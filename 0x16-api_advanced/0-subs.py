#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a subreddit
If an invalid subreddit is given, the function return 0
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    and returns the number of subscribers
    in a subreddit.
    - If an unvalid subreddit, return 0.
    """

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
