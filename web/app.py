"""
The `web/app.py` module is the main entry point for the web Flask application. It creates the Flask 
application, sets the configuration variables, and initializes the Flask-Login extension. It also
defines the `load_user` and `unauthorized_callback` functions for the Flask-Login extension.

The Flask application defines routes and views in the `web/views` package, which is imported at the 
end of this module.

Attributes:
    app (Flask): The Flask application object.
    login_manager (LoginManager): The Flask-Login extension object.

Usage:
To start the application, run the module from the main folder:

    $ python -m web.app

The application will be available at http://localhost:5000/.

"""
from flask import Flask, render_template, redirect, flash, url_for
from flask_login import LoginManager

from models import storage
from models.user import User

from flask_mail import Mail

from dotenv.main import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['APP_KEY']
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ['MAIL_USER']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASS']
mail = Mail(app)


@login_manager.user_loader
def load_user(user_id):
    """
    Load the user with the given ID from the storage engine.

    Args:
        user_id (str): The ID of the user to load.

    Returns:
        The User object with the given ID, or None if the user does not exist.
    """
    return storage.query(User, "id", user_id)

@login_manager.unauthorized_handler
def unauthorized_callback():
    """
    Handles unauthorized access to protected views.

    Returns:
        A redirect to the login page with a flashed message.
    """
    flash('Please Login to access this page.')
    return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors.

    Returns:
        A rendered 404 error page.
    """
    return render_template('404.html'), 404


from web.views import *


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)