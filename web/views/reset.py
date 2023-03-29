from web.app import app

from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user
from models import storage, User
from .utils import send_reset_email, verify_reset_token
from werkzeug.security import generate_password_hash

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        email = request.form.get('email')
        user = storage.query(User, 'email', email)
        if user is None:
            flash("email doesn't exist")
            return redirect(url_for('login'))
        send_reset_email(user)
        flash('An email has been sent with instruction to reset your password', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html')

@app.route('/reset/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    user_id = verify_reset_token(token)
    user = storage.get(User, user_id)
    if user is None:
        flash('Invalid or expired token')
        return redirect(url_for('reset_request'))
    if request.method == 'POST':
        newpassword = request.form.get('newpassword')
        renewpassword = request.form.get('renewpassword')

        if newpassword != renewpassword:
            flash("passwords doesn't match")
            return redirect(url_for('reset_token', token=token))
        hashed_password = generate_password_hash(newpassword)
        user.password = hashed_password
        user.save()
        flash('Your password has been updated!', 'info')
        return redirect(url_for('login'))
    return render_template('reset_token.html')