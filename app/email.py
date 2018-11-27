from flask_mail import Message
from flask import render_template
from . import mail
from .models import User

sender_email = 'projectsjeremy1000@gmail.com'
subject_pref_welcome = 'Welcome to DishiApp!'

def welcome_mail_message(subject, template, to, **kwargs):
  email = Message(subject_pref_welcome, sender=sender_email, recipients=[to])
  email.body = render_template(template+ '.txt', **kwargs)
  email.html = render_template(template+ '.html', **kwargs)
  mail.send(email)
