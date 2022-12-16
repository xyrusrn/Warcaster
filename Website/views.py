from flask import Blueprint, jsonify, render_template, flash, request, jsonify
from flask_login import login_required, current_user
from .models import Charnote, Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return jsonify({})

@views.route('/delete-char', methods=['POST'])
def delete_char():
    chardata = json.loads(request.data)
    charId = chardata['charId']
    chardata = Charnote.query.get(charId)
    if chardata:
        if chardata.user_id == current_user.id:
            db.session.delete(chardata)
            db.session.commit()
            return jsonify({})

@views.route('/notes', methods=['GET','POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note has been added!', category='success')
    return render_template("notes.html", user=current_user)

@views.route('/character', methods=['GET','POST'])
@login_required
def character():
    if request.method == 'POST':
        chardata = (request.form.get('editordata'))

        if len(chardata) < 1:
            flash('Note is too short!', category='error')

        else:
            new_data = Charnote(data=chardata, user_id=current_user.id)
            db.session.add(new_data)
            db.session.commit()
            flash('Note has been added!', category='success')
    return render_template("character.html", user=current_user)