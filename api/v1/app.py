"""
This `app` module is the main entry for the TeamZone API Flask application version 1.

It creates and configures a new Flask application, and registers various
routes and error handlers.

Routes:
- `status`: Returns the status of the API.

Error Handlers:
- `404`: Handles page not found errors with a custom error page.

Other:
- `close_session`: removes the current `sqlalchemy` session after every request


Configuration:
The application can be configured with the following environment variables:
- `APP_SETTINGS`: The configuration class to use (default is `config.DevelopmentConfig`).
- `DATABASE_URL`: The URL for the application's database (default is `sqlite:///data.db`).

Usage:
To start the application, run it the module from the main folder:

    $ python -m api.v1.app

The application will be available at http://localhost:5001/.
"""
from api.v1.views import app_views
from models import storage

from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app)


@app.route('/status')
def status():
    """
    Return a JSON object indicating the status of the application.

    Returns:
    A JSON object with a single key-value pair, where the key is "status"
    and the value is "OK".
    """
    return jsonify({"status": "OK"})

@app.errorhandler(404)
def not_found(error):
    """
    Handle a 404 error by returning a JSON error message.

    Args:
    error: The 404 error that occurred.

    Returns:
    A JSON object with a single key-value pair, where the key is "error"
    and the value is "Not found". The response status code is 404.
    """
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def close_session(exception):
    """
    Close the current SQLAlchemy session after each request.

    Args:
        exception: An optional exception that was raised during the request, if applicable.

    Returns:
        None.
    """
    storage.close()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)