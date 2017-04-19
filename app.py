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
    votes += crawler.crawl("http://woobox.com/2evorj/context/votepage?page=1&marker=52&ajax=1", me, votes)
    votes += crawler.crawl("http://woobox.com/2evorj/context/votepage?page=2&marker=52&ajax=1", me, votes)
    votes += crawler.crawl("http://woobox.com/2evorj/context/votepage?page=3&marker=52&ajax=1", me, votes)
    final_podium = crawler.get_podium(votes, me)
    return render_template('dinamic.html', me = me, ranking = final_podium)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)