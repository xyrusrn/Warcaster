from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from __init__ import create_app, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    with app.app_context():
        db.create_all() # create the SQLite database
    app.run(debug=True)
