from flask import Flask, render_template, request
from src import crawler
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    me = {
    "name": "Cristina M.",
    }
    votes = []
    total_pages = crawler.get_total_pages("http://woobox.com/2evorj/gallery")
    for page in range(1,total_pages):
        url = "http://woobox.com/2evorj/context/votepage?page={}&marker=52&ajax=1".format(page)
        votes += crawler.crawl(url, me, votes)
   
    final_podium = crawler.get_podium(votes, me)
    return render_template('dinamic.html', me = me, ranking = final_podium)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)