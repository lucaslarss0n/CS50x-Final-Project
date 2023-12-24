from flask import render_template, flash, redirect, url_for
from app import app
# if i need to import models:
# from app.models import User

@app.route('/signin')
def signin():
    return render_template('signin.html', title='Sign In')

@app.route('/register')
def register():
    return render_template('register.html', title='Register')

