"""
The `cities` module defines views for handling requests related to the `City` model.

This module defines the `cities` view, which handles GET, POST, PUT & DELETE requests 
for `City` objects. The view takes an optional `id` parameter to specify which `City` object to
retrieve or modify. If no `id` parameter is provided, the view will operate on all `City`
objects.

This module also defines the `countries_cities` view, which handles GET, POST, PUT & DELETE requests 
for `City` objects related to a specific `Country` object. The view takes a `country_id` parameter 
pointing to the `Country` object's `id`, and an optional `city_id` parameter to specify which `City`
object to retrieve or modify. If no `city_id` parameter is provided, the view will operate on all `City`
objects related to `Country`.

The `cities` & `countries_cities` view returns JSON-encoded responses.

See the views code for more detailed information on each method and its expected input and output.
"""
from api.v1.views import app_views
from models.city import City
from models.country import Country
from models import storage

from flask import abort, jsonify, request


@app_views.route('/cities', methods=['GET', 'POST'])
@app_views.route('/cities/<id>', methods=['GET', 'PUT', 'DELETE'])
def cities(id=None):
    """
    Handle HTTP requests for the City model.

    This view supports the following methods:
    - GET /cities: retrieve a list of all cities.
    - GET /cities/<id>: retrieve a city by its ID.
    - POST /cities: create a new city.
    - PUT /cities/<id>: update a city by its ID.
    - DELETE /cities/<id>: delete a city by its ID.

    Args:
    id (str): the ID of the city (optional, used only for single-city requests).

    Returns:
    The HTTP response containing the requested city(s), or an error message and status code if applicable.
    """
    if id:
        city = storage.get(City, id)
        if not city:
            abort(404)

    if request.method == 'GET':
        if id:
            return jsonify(city.to_dict())
        else:
            cities = [city.to_dict() for city in storage.all(City).values()]
            return jsonify(cities)
    
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        city_attributes = request.get_json()
        for attribute in ["name", "country_id"]:
            if attribute not in city_attributes:
                return jsonify({"error": f"Missing {str(attribute)}"}), 400
        new_city = City(**city_attributes)
        new_city.save()
        return jsonify(new_city.to_dict()), 201

    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        city_attributes = request.get_json()
        for key, value in city_attributes.items():
            if key not in ["id", "created_at", "updated_at", "country_id"]:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict())
    
    elif request.method == 'DELETE':
        city.delete()
        storage.save()
        return jsonify({})
    
@app_views.route('/countries/<country_id>/cities', methods=['GET', 'POST'])
@app_views.route('/countries/<country_id>/cities/<city_id>', methods=['GET', 'PUT', 'DELETE'])
def countries_cities(country_id, city_id=None):
    """
    Handle HTTP requests for the City model related to a specific Country.

    This view supports the following methods:
    - GET /countries/<country_id>/cities: retrieve a list of all cities for a specific country.
    - GET /countries/<country_id>/cities/<city_id>: retrieve a city by its ID for a specific country.
    - POST /countries/<country_id>/cities: create a new city for a specific country.
    - PUT /countries/<country_id>/cities/<city_id>: update a city by its ID for a specific country.
    - DELETE /countries/<country_id>/cities/<city_id>: delete a city by its ID for a specific country.

    Args:
    country_id (str): the ID of the country.
    city_id (str): the ID of the city (optional, used only for single-city requests).

    Returns:
    The HTTP response containing the requested city(s), or an error message and status code if applicable.
    """
    country = storage.get(Country, country_id)
    if not country:
        abort(404)
    if city_id:
        city = storage.get(City, city_id)
        if (not city) or (city not in country.cities):
            abort(404)
    
    if request.method == 'GET':
        if city_id:
            return jsonify(city.to_dict())
        else:
            cities = [city.to_dict() for city in country.cities]
            return jsonify(cities)
    
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        city_attributes = request.get_json()
        if "name" not in city_attributes:
            return jsonify({"error": "Missing name"}), 400
        city_attributes["country_id"] = str(country_id)
        new_city = City(**city_attributes)
        country.cities.append(new_city)
        country.save()
        new_city.save()
        return jsonify(new_city.to_dict()), 201
    
    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        city_attributes = request.get_json()
        for key, value in city_attributes.items():
            if key not in ["id", "created_at", "updated_at", "country_id"]:
                setattr(city, key, value)
        city.save()
        return jsonify(city.to_dict())
    
    elif request.method == 'DELETE':
        city.delete()
        storage.save()
        return jsonify({})