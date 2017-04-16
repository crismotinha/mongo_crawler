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
        print (content)