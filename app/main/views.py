from flask import render_template, request, redirect, url_for, abort, flash, session, jsonify
from . import main
from ..models import User, Recipes, Favourites
from flask_login import login_required, current_user
from .. import db
from datetime import datetime

# Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  return render_template('index.html')

@main.route('/users', methods=['GET', 'POST'])
def get_users():
  users = User.query.all()
  ei="id"
  un="username"
  d4=[]
  for user in users:
    d3={ei:user.id, un:user.username}
    d4.append(d3)
  return jsonify({'users':d4})

@main.route('/recipes', methods=['GET', 'POST'])
def get_recipes():
  recipes = Recipes.query.all()
  ca = "category"
  re = "recipe"
  ui = "username"
  d4 = []
  for recipe in recipes:
    d3 = {ca: recipe.category, re: recipe.recipe, ui: User.get_user(recipe.user_id)}
    d4.append(d3)
  return jsonify({'recipes':d4})
  