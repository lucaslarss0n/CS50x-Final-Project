from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user
from app import db
from app.models import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form_data = {}
    if request.method == 'POST':
        form_data['username'] = request.form.get('username')
        form_data['password'] = request.form.get('password')

        user = User.query.filter_by(username=form_data['username']).first()

        if user and user.check_password(form_data['password']):
            login_user(user)
            flash('Login successful.', 'success')
            return redirect(url_for('main_bp.index'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html', form_data=form_data)

@auth_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main_bp.index'))

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form_data = {}
    if request.method == 'POST':
        form_data['username'] = request.form.get('username')
        form_data['password'] = request.form.get('password')
        form_data['password_confirm'] = request.form.get('password_confirm')

        if User.query.filter_by(username=form_data['username']).first():
            flash('Username already exists. Please try again.', 'error')
            return redirect(url_for('auth_bp.register'))

        if len(form_data['password']) < 8:
            flash('Password must be at least 8 characters.', 'error')
            return redirect(url_for('auth_bp.register'))
        elif len(form_data['password']) > 40:
            flash('Password must be less than 40 characters.', 'error')
            return redirect(url_for('auth_bp.register'))

        if form_data['password'] == form_data['password_confirm']:
            new_user = User(username=form_data['username'])
            new_user.set_password(form_data['password'])
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. Please log in.', 'success')
            return redirect(url_for('auth_bp.login'))
        else:
            flash('Passwords do not match. Please try again.', 'error')

    return render_template('register.html', title='Register', form_data=form_data)
