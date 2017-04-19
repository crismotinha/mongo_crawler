import urllib.request
from bs4 import BeautifulSoup
import json
import re

import requests

def get_total_pages(url):
    url = 'https://woobox.com/2evorj/context/votepage?page=0'
    r = requests.get(url).json()
    return r.get('offer').get('uploads').get('paging').get('total_pages')


def crawl(url, me, votes_list):
    r = requests.get(url).json()
    contestants = r['offer']['uploads']['data']
    return votes_list = [
            { 
                "contestant": contestant['uploaded_by'],
                "votes": int(contestant["votes"])
            }
            for contestant in contestants]


def get_podium(newlist, me):
    newlist = sorted(newlist, key=lambda k: k['votes'], reverse=True)
    for i in newlist:
        if i['contestant'] == me["name"]:
            me["position"] = newlist.index(i) + 1
    return {'first':
    {"name":newlist[0]["contestant"],
    "votes": newlist[0]["votes"]},
    'second':
    {"name":newlist[1]["contestant"],
    "votes": newlist[1]["votes"]},
    'third':
    {"name":newlist[2]["contestant"],
    "votes": newlist[2]["votes"]},
    }
