import functools
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify
from flask import request
from flask_jwt_extended.utils import create_access_token

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    db = get_db()
    error = None
    
    if not email:
        error = 'Email is required'
    elif not password:
        error = 'Password is required'
    elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        error = 'Invalid email'
    elif db.execute(
        'SELECT email FROM user WHERE email = ?', (email,)
    ).fetchone() is not None:
        error = f"Email {email} is already registered."

    if error is None:
        db.execute(
            'INSERT INTO user (email, password) VALUES (?, ?)',
            (email, generate_password_hash(password))
        )
        db.commit()

        redirect(url_for('auth.login'))

        return jsonify({'msg': 'registered'}), 201
    
    return jsonify({'msg': error}), 400
    
    
@bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    db = get_db()
    user = None
    error = None
    
    if not email:
        error = 'Email is required'
    elif not password:
        error = 'Password is required'
    elif not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        error = 'Invalid email'
    else:
        user = db.execute(
            'SELECT * FROM user WHERE email = ?', (email,)
            ).fetchone()

    if user is None:
        error = 'Incorrect email'
    elif not check_password_hash(user['password'], password):
        error = 'Incorrect password'

    if error is None:
        access_token = create_access_token(identity=user['id'])
        session.clear()
        session['user_id'] = user['id']
        return jsonify(access_token=access_token), 201
    
    return jsonify({"msg": error}), 400