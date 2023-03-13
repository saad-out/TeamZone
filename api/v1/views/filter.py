"""
The `filter` module defines a view for handling requests related to filtering `Team` objects.

This module defines the `filter_teams` view, which handles POST requests for filtering `Team`
objects based on a given `country`, `city`, and `sport` in the request's JSON payload.

The `filter_teams` view returns a JSON-encoded response containing a list of `Team` objects
that match the specified filters, or an empty list if no matching `Team` objects are found.

See the view code for more detailed information on the expected input and output.
"""
from api.v1.views import app_views
from models import storage
from models.country import Country
from models.city import City
from models.sport import Sport
from models.team import Team

from flask import abort, jsonify, request


@app_views.route('/filter_teams', methods=['POST'])
def filter_teams():
    """
    This view filters `Team` objects by country, city, and sport.

    The view takes a POST request with a JSON payload containing the following keys:
    - countries: a list of `Country` ids to filter teams by
    - cities: a list of `City` ids to filter teams by
    - sports: a list of `Sport` ids to filter teams by

    The view then returns a JSON response containing a list of `Team` objects that match the
    specified filter parameters. If no filter parameters are provided, all `Team` objects are returned.

    Returns:
        A JSON response containing a list of `Team` objects that match the specified filter parameters.
    """

    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    else:
        filter_parameters = request.get_json()
    
    country_ids = filter_parameters.get('countries', [])
    city_ids = filter_parameters.get('cities', [])
    sport_ids = filter_parameters.get('sports', [])

    cities = []
    for country_id in country_ids:
        country = storage.get(Country, country_id)
        if country:
            for city in country.cities:
                cities.append(city)
    for city_id in city_ids:
        city = storage.get(City, city_id)
        if city and (city not in cities):
            cities.append(city)

    teams_by_locations = []
    if cities or country_ids or city_ids:
        for city in cities:
            for team in city.teams:
                teams_by_locations.append(team)
    else:
        teams_by_locations = [team for team in storage.all(Team).values()]
    
    if sport_ids:
        filtered_teams = [team.to_dict() for team in teams_by_locations if (team.sport_id in sport_ids)]
    else:
        filtered_teams = [team.to_dict() for team in teams_by_locations]

    return jsonify(filtered_teams)