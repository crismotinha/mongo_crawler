import urllib.request
from bs4 import BeautifulSoup
import json
import re

def crawl(url, me, votes_list):
    page = urllib.request.urlopen(url)
    # soup = BeautifulSoup(page, "html.parser")
    # raw_content = soup.decode("utf-8")
    content = json.loads(page.read().decode('utf-8'), strict=False)
    contestants = content['offer']['uploads']['data']
    votes_list = []
    for contestant in contestants:
        if contestant['uploaded_by'] == me["name"]:
            me["pic"] = contestant['url']
        votes_list.append({"contestant":contestant['uploaded_by'], "votes":int(contestant["votes"])})
    return votes_list


def get_podium(newlist, me):
    print(newlist)
    newlist = sorted(newlist, key=lambda k: k['votes'], reverse=True)
    for i in newlist:
        if i['contestant'] == me["name"]:
            me["position"] = newlist.index(i) + 1
    print(newlist)
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