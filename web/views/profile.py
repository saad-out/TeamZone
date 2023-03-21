"""
This module contains Flask views for handling user profile related requests.

This module defines the following views:
    - POST /change_password: allows a user to change their password if they are logged in.
    - POST /profile_edit: allows a user to edit their profile details such as name, username, email, and profile picture.
    
See the views code for more detailed information on each method and its expected input and output.
"""
from web.app import app

from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team, User
from .utils import save_image

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
    """
    Handle changing password requests.

    This view supports the following methods:
        - POST /change_password: change the password of the current user.

    Returns:
    A redirection to the profile page with a flash message indicating if the update was successful or not.
    """
    password = request.form.get('password')
    newpassword = request.form.get('newpassword')
    renewpassword = request.form.get('renewpassword')
    if newpassword != renewpassword:
        flash("New password doesn't match")
        return redirect(url_for('profile'))
    user = storage.get(User, current_user.id)
    if user.password != password:
        flash("Incorrect password")
        return redirect(url_for('profile'))
    user.password = newpassword
    user.save()
    return redirect(url_for('profile'))


@app.route('/profile_edit', methods=['POST'])
@login_required
def profile_edit():
    """
    Handle profile edit requests.

    This view supports the following methods:
        - POST /profile_edit: update the attributes of the current user.

    Returns:
    A redirection to the profile page with a flash message indicating if the update was successful or not.
    """
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    filename = ''
    reset = 'reset-picture' in request.form
    if not reset:
        image = request.files['image']
        filename = save_image(image, 'users', current_user.id)
    else:
        filename = "user_default.jpg"
    user = storage.get(User, current_user.id)
    if user:
        try:
            user.name = name
            user.email = email
            user.username = username
            if filename != "":
                user.image = filename
            user.save()
        except Exception as e:
            if 'username' in str(e).split('\n')[1]:
                flash("username exists")
            else:
                flash("email exists")
            return redirect(url_for('profile'))
    return redirect(url_for('profile'))