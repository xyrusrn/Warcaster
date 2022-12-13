from flask import (Flask, request, redirect, session, render_template, url_for)

app = Flask (__name__)
app.secret_key = 'SecretKey'
user = {"username", "abc", "password", "xyz"}

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login/", methods = ['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == user['username'] and password == user['password']:

            session['user'] = username
            return redirect('/dashboard/')
        return "Wrong username or password"
    
    return render_template("login.html")

