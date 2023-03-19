from web.app import app

from flask import render_template, request, url_for, redirect, flash
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team, User
from .utils import save_image

@app.route('/change_password', methods=['POST'])
@login_required
def change_password():
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