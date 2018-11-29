import unittest
from app.models import Recipes
from datetime import datetime

class RecipeTest(unittest.TestCase):

  def setUp(self):
    self.new_recipe = Recipes(1, 'title', 'body', 'j')

  def tearDown(self):
    Recipes.query.delete()

  def test_instance(self):
    self.assertTrue(isinstance(self.new_recipe, Recipes))

  def test_save_recipe(self):
    self.new_recipe.save_recipe()
    self.assertTrue(len(Recipes.query.all())>0)

  def test_get_posts(self):
    self.new_post.save_post()
    got_post = Recipes.find_specific_by_id(1)
    self.assertTrue(len(got_post) == 1)

  def test_get_all_recipes(self):
    self.new_recipe.save_recipe()
    self.new_recipe1 = Recipes(2, 'title', 'body', 
    'j')
    self.new_recipe1.save_recipe()
    got_recipes = Recipes.get_recipes()
    self.assertTrue(len(got_recipes) == 2)
