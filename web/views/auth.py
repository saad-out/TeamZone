"""
The `auth` module defines views for handling authentication requests.

This module defines the following views:
    - `login()`: handles user login requests.
    - `signout()`: handles user logout requests.
    - `signup()`: handles user signup requests.

See the views code for more detailed information on each method and its expected input and output.
"""
from web.app import app
from web.views.utils import verify_recaptcha
from models import storage
from models.user import User

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle login requests.

    This view supports the following methods:
        - GET /login: retrieve a login form.
        - POST /login: attempt to authenticate the user using the provided email and password.

    Returns:
    If a GET request is received, returns a rendered login template. If a POST request is received and the user is
    authenticated, redirects to the dashboard page. Otherwise, redirects back to the login page with an error message.
    """
    next = request.args.get('next')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        recaptcha_response = request.form.get('reCAPTCHA')

        if not verify_recaptcha(recaptcha_response):
            flash('Please verify that you are not a robot.', 'error')
            return redirect(url_for('login'))

        user = storage.query(User, "email", email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(next or url_for('dashboard'))
        else:
            flash('Invalid credentials! Try again.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html', next=next, recaptcha_site_key=os.getenv('RECAPTCHA_SITE_KEY'))

@app.route('/signup', methods=['POST'])
def signup():
    """
    Handle HTTP requests for the sign up view.

    This view supports the following method:
        - POST /signup: create a new user.

    Returns:
        The HTTP response containing a message indicating whether the user was created successfully, or an error message if applicable.
    """
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    recaptcha_response = request.form.get('reCAPTCHA')

    if not verify_recaptcha(recaptcha_response):
        flash('Please verify that you are not a robot.', 'error')
        return redirect(url_for('login'))

    if password != confirm_password:
        flash('Please use the same password in both password fields.', 'error')
        return redirect(url_for('login'))
    
    user_by_email = storage.query(User, "email", email)
    user_by_username = storage.query(User, "username", username)
    if not user_by_email and not user_by_username:
        user_attributes = {
                        "name": name,
                        "email": email,
                        "username": username,
                        "password": generate_password_hash(password)
                        }
        new_user = User(**user_attributes)
        new_user.save()
        flash('Account created successfully!', 'info')
    else:
        flash('This user already exists!', 'error')
    
    return redirect(url_for('login'))


@app.route('/signout')
@login_required
def signout():
    """
    Handle HTTP requests for the sigout view.

    This view supports the following method:
        - GET /signout: log out the user.

    Returns:
        The HTTP response is a redirection to the login page.
    """
    logout_user()
    return redirect(request.args.get('next') or url_for('login'))