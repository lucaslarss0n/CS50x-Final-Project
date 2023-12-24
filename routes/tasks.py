from flask import render_template, flash, redirect, url_for
from app import app
# import forms and models if needed

@app.route('/tasks')
def tasks():
    # Logic to display tasks
    return render_template('tasks.html')