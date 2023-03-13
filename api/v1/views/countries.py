"""
The `countries` module defines views for handling requests related to the `Country` model.

This module defines the `countries` view, which handles GET, POST, PUT & DELETE requests 
for `Country` objects. The view takes an optional `id` parameter to specify which `Country` object to
retrieve or modify. If no `id` parameter is provided, the view will operate on all `Country`
objects.

The view return JSON-encoded responses.

See the views code for more detailed information on each method and its expected input and output.
"""

from api.v1.views import app_views
from models.country import Country
from models import storage

from flask import abort, jsonify, request


@app_views.route('/countries', methods=['GET', 'POST'])
@app_views.route('/countries/<id>', methods=['GET', 'PUT', 'DELETE'])
def countries(id=None):
    """
    Handle HTTP requests for the Country model.

    This view supports the following methods:
        - GET /countries: retrieve a list of all countries.
        - GET /countries/<id>: retrieve a country by its ID.
        - POST /countries: create a new country.
        - PUT /countries/<id>: update a country by its ID.
        - DELETE /countries/<id>: delete a country by its ID.

    Args:
        id (str): the ID of the country (optional, used only for single-country requests).

    Returns:
        The HTTP response containing the requested country(ies), or an error message and status code if applicable.
    """
    if id:
        country = storage.get(Country, id)
        if not country:
            abort(404)
    
    if request.method == 'GET':
        if id:
            return jsonify(country.to_dict())
        else:
            countries = [country.to_dict() for country in storage.all(Country).values()]
            return jsonify(countries)
    
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        country_attributes = request.get_json()
        if "name" not in country_attributes:
            return jsonify({"error": "Missing name"}), 400
        new_country = Country(**country_attributes)
        new_country.save()
        return jsonify(new_country.to_dict()), 201

    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        country_attributes = request.get_json()
        for key, value in country_attributes.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(country, key, value)
        country.save()
        return jsonify(country.to_dict())

    elif request.method == 'DELETE':
        country.delete()
        storage.save()
        return jsonify({})