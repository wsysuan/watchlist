from unicodedata import name
from flask import Flask
from flask import url_for


app = Flask(__name__)


@app.route('/')
def index_page():
    return 'hello world'
