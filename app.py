from flask import (Flask, request, redirect, session, render_template)

app = Flask (__name__)
app.secret_key = 'SecretKey'
user = {"username", "abc", "password", "xyz"}

@app.route("/login")
def login():
    return "Forced Login"

