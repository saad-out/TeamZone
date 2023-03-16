from web.app import app

from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from models import storage
from models.user import User


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = storage.query(User, "email", email)
        if user and (password == user.password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        return redirect(url_for('login'))
    
    user = storage.query(User, "email", email)
    if not user:
        user_attributes = {
                        "name": name,
                        "email": email,
                        "username": username,
                        "password": password
                        }
        print(user_attributes)
        new_user = User(**user_attributes)
        new_user.save()
    
    return redirect(url_for('login'))


@app.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('login'))