import urllib.request
from bs4  import BeautifulSoup
import json
import re

page = urllib.request.urlopen("http://woobox.com/2evorj/gallery/HOrALzX1uVs")
soup = BeautifulSoup(page, "html.parser")

pattern = re.compile('var context = (.*\s\S.*);')
scripts = soup.find_all('script')
for script in scripts:
    if(pattern.search(str(script.string))):
        data = pattern.search(script.string)
        content = json.loads(data.groups()[0])

contestants = content['offer']['uploads']['data']
votes = []

me = {
    "name": "Cristina M.",
}

for contestant in contestants:
    if contestant['uploaded_by'] == me["name"]:
        me["pic"] = contestant['url']
    votes.append({"contestant":contestant['uploaded_by'], "votes":contestant["votes"]})

newlist = sorted(votes, key=lambda k: k['votes'], reverse=True) 

for i in newlist:
    if i['contestant'] == me["name"]:
        me["position"] = newlist.index(i) + 1

def get_podium():
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

def get_me():
    return me