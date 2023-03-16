from flask import Flask, render_template
from flask_login import LoginManager

from models import storage
from models.user import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return storage.query(User, "id", user_id)

from web.views import *


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)