from os import getenv

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi there"

@app.route("/home/")
def home():
    return "Home page"

@app.route("/lore/")
def lore():
    return "Lore page"