from flask import render_template, flash, redirect, url_for
from app import app
# if i need to import models:
# from app.models import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title='login')

from flask import request, flash, redirect, url_for

@app.route('/register', methods=['GET', 'POST'])
def register():
    form_data = {}
    if request.method == 'POST':
        form_data['username'] = request.form.get('username')
        password = request.form.get('password')
        password_confirm = request.form.get('password_confirm')

        # Add your validation and registration logic here

        # Example validation: Check if username already exists
        if User.query.filter_by(username=form_data['username']).first():
            flash('Username already exists. Please try again.', 'error')
            return redirect(url_for('register'))
        
        # Example validation: Check if passwords match
        if password == password_confirm:
            # Assuming User is your user model and it has a register method
            User.register(form_data['username'], password)
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match. Please try again.', 'error')

        # Password validation
        if len(password) < 8:
            flash('Password must be at least 8 characters.', 'error')
            return redirect(url_for('register'))
        elif len(password) > 50:
            flash('Password must be less than 50 characters.', 'error')
            return redirect(url_for('register'))
        

    return render_template('register.html', title='Register', form_data=form_data)

