from web.app import app

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from models import storage
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/login', methods=['GET', 'POST'])
def login():
    next = request.args.get('next')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = storage.query(User, "email", email)
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(next or url_for('search'))
        else:
            flash('Invalid credentials! Try again.', 'error')
            return redirect(url_for('login'))
    
    return render_template('login.html', next=next)

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

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
    logout_user()
    return redirect(request.args.get('next') or url_for('login'))