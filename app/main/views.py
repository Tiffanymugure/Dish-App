from flask import render_template, request, redirect, url_for, abort, flash, session, jsonify
from . import main
from ..models import User, Recipes, Favourites
from flask_login import login_required, current_user
from .. import db
from datetime import datetime



# Views
@main.route('/')
def index():
    users = User.query.all()
    print(users)

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html', users=users)

@main.route('/users')
def get_users():
  users = User.query.all()
  new_users= [(user.username, user.pass_secure) for user in users]
  d = {key: value for (key, value) in new_users}
  return jsonify({'users':d})
