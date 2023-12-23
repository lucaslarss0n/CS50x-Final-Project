from flask import render_template, flash, redirect, url_for
from app import app
# if i need to import models:
# from app.models import User

@app.route('/login')
def login():
    form = # Your LoginForm
    return render_template('auth/login.html', title='Sign In', form=form)

@app.route('/register')
def register():
    form = # Your RegistrationForm
    return render_template('auth/register.html', title='Register', form=form)