from flask import (Flask, request, redirect, session, render_template, url_for)

app = Flask (__name__)
app.secret_key = 'SecretKey'
user = {"username", "abc", "password", "xyz"}

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login/")
def login():
    return "Forced Login"

