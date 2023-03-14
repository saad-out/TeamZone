"""
The `views` package contains Flask blueprints for various parts of the application.

This package defines the `app_views` blueprint for the application's views.

Blueprints:
- `app_views`: A blueprint for the application's views.

Usage:
The blueprints defined in this package can be registered with the Flask application
in the main entry point (`app.py`) as follows:

    app.register_blueprint(app_views)

This will register the `app_views` blueprint with the Flask application, making its routes
available at the URL prefix `/api/v1`.

See the Flask documentation for more information on using blueprints:
http://flask.palletsprojects.com/en/2.1.x/blueprints/
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.teams import *
from api.v1.views.filter import *
from api.v1.views.sports import *
from api.v1.views.countries import *
from api.v1.views.cities import *