import urllib.request
from bs4  import BeautifulSoup
import json
import re

def crawl(url, me):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")

    pattern = re.compile('var context = (.*\s\S.*);')
    scripts = soup.find_all('script')
    for script in scripts:
        if(pattern.search(str(script.string))):
            data = pattern.search(script.string)
            content = json.loads(data.groups()[0])

    contestants = content['offer']['uploads']['data']
    votes = []
    for contestant in contestants:
        if contestant['uploaded_by'] == me["name"]:
            me["pic"] = contestant['url']
        votes.append({"contestant":contestant['uploaded_by'], "votes":contestant["votes"]})

    newlist = sorted(votes, key=lambda k: k['votes'], reverse=True) 

    for i in newlist:
        if i['contestant'] == me["name"]:
            me["position"] = newlist.index(i) + 1

    return newlist


def get_podium(newlist):
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
