from os import getenv

from flask import Flask
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    return "Hi there"

@app.route("/login/")
def home():
    return "Login page"

@app.route("/home/")
def home():
    return "Home page"

@app.route("/lore/")
def lore():
    return "Lore page"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='Ryan Nieboer'))