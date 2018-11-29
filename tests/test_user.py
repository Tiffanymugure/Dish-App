import unittest
from app.models import User
from datetime import datetime

class UserModelTest(unittest.TestCase):

  def setUp(self):
    self.new_user=User(1, 'jeremy', 'j@j.com', datetime.now(),  password='banana')

  def tearDown(self):
    User.query.delete()

  def test_password_setter(self):
    self.assertTrue(self.new_user.pass_secure is not None)

  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password

  def test_password_verfication(self):
    self.assertTrue(self.new_user.verify_password('banana'))

  def test_save_user(self):
    self.new_user.save_user()
    self.assertTrue(len(User.query.all())>0)

  def test_get_users(self):
    self.new_user.save_user()
    self.new_user1=User(2, 'jeremy', 'j@m.com', datetime.now(), password='banana')
    self.new_user1.save_user()
    users = User.get_users()
    self.assertTrue(len(User.query.all()) == 2)

  def test_master(self):
    master = User.init_db()
    all_users = User.query.all()
    self.assertTrue(len(all_users) == 1)

  