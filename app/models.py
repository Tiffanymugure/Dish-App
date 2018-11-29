from flask import jsonify
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  __tablename__='users'


  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255))
  joined=db.Column(db.DateTime,default=datetime.now)
  pass_secure = db.Column(db.String(255))

  recipes = db.relationship('Recipes', backref='recipes', lazy='dynamic')
  favourites = db.relationship('Favourites', backref='user_favourites', lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You do not have the permissions to access this')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self, password):
    return check_password_hash(self.pass_secure, password)

  def save_user(self):
    db.session.add(self)
    db.session.commit()

  def init_db():
    if User.query.count() == 0:
      master = User(username='master', password='master', email='projectsjeremy1000@gmail.com')
      
      db.session.add(master)
      db.session.commit()

  @classmethod
  def get_user(cls, id):
    user = cls.query.filter_by(id=id).first()
    return user.username

  @classmethod
  def get_users(cls):
    users = User.query.all()
    return users


class Recipes(UserMixin, db.Model):
  __tablename__='recipes'

  id = db.Column(db.Integer, primary_key = True)
  category  = db.Column(db.String(255))
  recipe = db.Column(db.String)
  image_path = db.Column(db.String)
  
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_recipe(self):
    db.session.add(self)
    db.session.commit()

  def find_specific_by_id(id):
    recipe = Recipes.query.filter_by(id=id).first()
    return recipe


  def init_db_recipe():
    if Recipes.query.count() == 0:
      default = Recipes(category='default', recipe='default recipe', image_path='image_path', user_id=1)
      default1 = Recipes(category='default', recipe='default recipe 2', image_path='image_path', user_id=1)
      db.session.add_all([default, default1])
      db.session.commit()


  @classmethod
  def get_recipes(cls):
    recipes = Recipes.query.all()
    return recipes  

class Favourites(UserMixin, db.Model):
  __tablename__='favourites'

  id = db.Column(db.Integer, primary_key  = True)

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_recipe(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_recipes(cls, id):
    favourites = Favourites.query.filter_by(user_id=id)
    return recipes  

