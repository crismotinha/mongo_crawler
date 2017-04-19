import urllib.request
from bs4 import BeautifulSoup
import json
import re

def get_total_pages(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    pattern = re.compile('var context = (.*\s\S.*);')
    scripts = soup.find_all('script')
    for script in scripts:
        if(pattern.search(str(script.string))):
            data = pattern.search(script.string)
            content = json.loads(data.groups()[0])
    if 'total_pages' in content['offer']['uploads']['paging']:
        return content['offer']['uploads']['paging']['total_pages']
    else:
        return 10

def crawl(url, me, votes_list):
    page = urllib.request.urlopen(url)
    content = json.loads(page.read().decode('utf-8'), strict=False)
    contestants = content['offer']['uploads']['data']
    votes_list = []
    for contestant in contestants:
        if contestant['uploaded_by'] == me["name"]:
            me["pic"] = contestant['url']
        votes_list.append({"contestant":contestant['uploaded_by'], "votes":int(contestant["votes"])})
    return votes_list


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