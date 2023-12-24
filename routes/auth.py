from flask import render_template, flash, redirect, url_for
from app import app
# if i need to import models:
# from app.models import User

@app.route('/signin')
def login():
    return render_template('auth/signin.html', title='Sign In')

@app.route('/register')
def register():
    return render_template('auth/register.html', title='Register')