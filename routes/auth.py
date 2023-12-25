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

        if password == password_confirm:
            # Assuming User is your user model and it has a register method
            User.register(form_data['username'], password)
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match. Please try again.', 'error')

    return render_template('register.html', title='Register', form_data=form_data)

