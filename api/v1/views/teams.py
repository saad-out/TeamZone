"""
The `teams` module defines views for handling requests related to the `Team` model.

This module defines the `teams` view, which handles GET, POST, PUT, and DELETE requests for
`Team` objects. The view takes an optional `id` parameter to specify which `Team` object to
retrieve or modify. If no `id` parameter is provided, the view will operate on all `Team`
objects.

The module also defines the `users_teams` view, which handles GET, POST, PUT, and DELETE requests for
`Team` objects related to a specific `User` object. The view takes a `user_id` parameter pointing to
the `User` object's `id`, and an optional `team_id` parameter to specify which `Team` object to
retrieve or modify. If no `id` parameter is provided, the view will operate on all `Team`
objects related to `User`.


The `teams` & `users_teams` view returns JSON-encoded responses

See the views code for more detailed information on each method and its expected input and output.
"""

from api.v1.views import app_views
from models import storage
from models.team import Team
from models.user import User
from models.city import City
from models.country import Country

from flask import abort, jsonify, request


@app_views.route('/teams', methods=['GET', 'POST'])
@app_views.route('/teams/<id>', methods=['GET', 'PUT', 'DELETE'])
def teams(id=None):
    """Handle HTTP requests for the Team model.

    This view supports the following methods:
        - GET /teams: retrieve a list of all teams.
        - GET /teams/<id>: retrieve a team by its ID.
        - POST /teams: create a new team.
        - PUT /teams/<id>: update a team by its ID.
        - DELETE /teams/<id>: delete a team by its ID.

    Args:
        id (str): the ID of the team (optional, used only for single-team requests).

    Returns:
        The HTTP response containing the requested team(s), or an error message and status code if applicable.
    """
    if id:
        team = storage.get(Team, id)
        if not team:
            abort(404)

    if request.method == 'GET':
        if id:
            return jsonify(team.to_dict())
        else:
            teams = [team.to_dict() for team in storage.all(Team).values()]
            return jsonify(teams)
    
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        team_attributes = request.get_json()
        for attribute in ["name", "sport_id", "city_id", "leader_id"]:
            if attribute not in team_attributes:
                return jsonify({"error": f"Missing {str(attribute)}"}), 400
        new_team = Team(**team_attributes)
        new_team.save()
        return jsonify(new_team.to_dict()), 201
    
    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        team_attributes = request.get_json()
        for key, value in team_attributes.items():
            if key not in ["id", "created_at", "updated_at", "leader_id"]:
                setattr(team, key, value)
        team.save()
        return jsonify(team.to_dict())
    
    elif request.method == 'DELETE':
        team.delete()
        storage.save()
        return jsonify({})
    

@app_views.route('/users/<user_id>/teams', methods=['GET', 'POST'])
@app_views.route('/users/<user_id>/teams/<team_id>', methods=['GET', 'PUT', 'DELETE'])
def users_teams(user_id, team_id=None):
    """Handle HTTP requests for the Team model related to User object.

    This view supports the following methods:
        - GET /users/<user_id>/teams: retrieve a list of all teams for user.
        - GET /users/<user_id>/teams/<team_id>: retrieve a team by its ID for user.
        - POST /users/<user_id>/teams: create a new team for user.
        - PUT /users/<user_id>/teams/<team_id>: update a team by its ID for user.
        - DELETE /users/<user_id>/teams/<team_id>: delete a team by its ID for user.

    Args:
        user_id (str): the ID of the user.
        team_id (str): the ID of the team (optional, used only for single-team requests).

    Returns:
        The HTTP response containing the requested team(s), or an error message and status code if applicable.
    """
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if team_id:
        team = storage.get(Team, team_id)
        if (not team) or (team not in user.teams):
            abort(404)
    
    if request.method == 'GET':
        if team_id:
            return jsonify(team.to_dict())
        else:
            teams = [team.to_dict() for team in user.teams]
            return jsonify(teams)
    
    elif request.method == 'POST':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        team_attributes = request.get_json()
        for attribute in ["name", "country", "city", "sport_id", "bio"]:
            if attribute not in team_attributes:
                return jsonify({"error": f"Missing {str(attribute)}"}), 400
            
        team_country = storage.query(Country, "name", team_attributes.get("country"))
        if not team_country:
            team_country = Country(name=team_attributes.get("country"))
            team_country.save()
        team_city = storage.query(City, "name", team_attributes.get("city"))
        if not team_city:
            team_city = City(name=team_attributes.get("city"), country_id=team_country.id)
            team_city.save()

        new_team = {
            "name": team_attributes.get("name"),
            "sport_id": team_attributes.get("sport_id"),
            "city_id": team_city.id,
            "leader_id": user_id,
            "bio": team_attributes.get("bio")
        }
        new_team = Team(**new_team)
        new_team.players.append(user)
        new_team.save()
        return jsonify(new_team.to_dict()), 201
    
    elif request.method == 'PUT':
        if not request.is_json:
            return jsonify({"error": "Not a JSON"}), 400
        team_attributes = request.get_json()

        team_country = storage.query(Country, "name", team_attributes.get("country"))
        if not team_country:
            team_country = Country(name=team_attributes.get("country"))
            team_country.save()
        team_city = storage.query(City, "name", team_attributes.get("city"))
        if not team_city:
            team_city = City(name=team_attributes.get("city"), country_id=team_country.id)
            team_city.save()
        
        updated_team = {
            "name": team_attributes.get("name"),
            "sport_id": team_attributes.get("sport_id"),
            "city_id": team_city.id,
            "image": team_attributes.get("image"),
            "bio": team_attributes.get("bio")
        }

        for key, value in updated_team.items():
            if value:
                setattr(team, key, value)
        team.save()
        return jsonify(team.to_dict())
    
    elif request.method == 'DELETE':
        team.delete()
        storage.save()
        return jsonify({})
