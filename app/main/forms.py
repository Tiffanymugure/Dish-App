from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class RecipeForm(FlaskForm):
  title=StringField('Recipe Title')
  body=TextAreaField('Write Away')
  submit=SubmitField('Submit')

