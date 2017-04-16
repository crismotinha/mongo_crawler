from flask import Flask, render_template, request
from src import crawler
import os


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('dinamic.html', me = crawler.get_me(), ranking = crawler.get_podium())

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)