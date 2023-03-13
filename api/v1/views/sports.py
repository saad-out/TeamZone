"""
The `sports` module defines views for handling requests related to the `Sport` model.

This module defines the `sports` view, which handles GET, POST, PUT & DELETE requests 
for `Sport` objects. The view takes an optional `id` parameter to specify which `Sport` object to
retrieve or modify. If no `id` parameter is provided, the view will operate on all `Sport`
objects.

The view return JSON-encoded responses.

See the views code for more detailed information on each method and its expected input and output.
"""
from api.v1.views import app_views
from models import storage
from models.sport import Sport

from flask import abort, jsonify, request


@app_views.route('/sports', methods=['GET', 'POST'])
@app_views.route('/sports/<id>', methods=['GET', 'PUT', 'DELETE'])
def sports(id=None):
    """Handle HTTP requests for the Sports model.

    This view supports the following methods:
    - GET /sports: retrieve a list of all sports.
    - GET /sports/<id>: retrieve a sport by its ID.
    - POST /sports: create a new sport.
    - PUT /sports/<id>: update a sport by its ID.
    - DELETE /sports/<id>: delete a sport by its ID.

    Args:
    id (str): the ID of the sport (optional, used only for single-sport requests).

    Returns:
    The HTTP response containing the requested sport(s), or an error message and status code if applicable.
    """
    if id:
        sport = storage.get(Sport, id)
        if not sport:
            abort(404)

    if request.method == 'GET':
        if id:
            return jsonify(sport.to_dict())
        else:
            sports = [sport.to_dict() for sport in storage.all(Sport).values()]
            return jsonify(sports)
    
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        sport_attributes = request.get_json()
        if "name" not in sport_attributes:
            return jsonify({"error": "Missing name"}), 400
        new_sport = Sport(**sport_attributes)
        new_sport.save()
        return jsonify(new_sport.to_dict()), 201
    
    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        sport_attributes = request.get_json()
        for key, value in sport_attributes.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(sport, key, value)
        sport.save()
        return jsonify(sport.to_dict())
    
    elif request.method == 'DELETE':
        sport.delete()
        storage.save()
        return jsonify({})