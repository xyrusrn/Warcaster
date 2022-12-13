from flask import (Flask, request, redirect, session, render_template, url_for, flash)
import os

app = Flask (__name__)  
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
            return redirect (url_for('dashboard'))
        return "Wrong username or password"
    
    return render_template("login.html")

@app.route("/dashboard/")
def dashboard():
    if ('user' in session and session ['user'] == user['username']):
        return "Welcome to the dashboard!"
    
    return "You are not logged in."

@app.route('/logout')
def logout():
    session.pop('user')         
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key = os.urandom(12)  
    app.run(debug=True)
