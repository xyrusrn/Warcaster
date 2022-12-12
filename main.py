from os import getenv

from flask import Flask

from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app

main = Blueprint('main', __name__)
@main.route('/')
def index():
    return 'index'


@main.route('/profile')
def profile():
    return 'profile'

app = create_app()
app.run(debug=True)