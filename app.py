from flask import Flask, render_template, request
from src import crawler
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    me = {
    "name": "Cristina M.",
    }
    podium = crawler.crawl("http://woobox.com/2evorj/gallery/HOrALzX1uVs", me)
    return render_template('dinamic.html', me = me, ranking = crawler.get_podium(podium))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)