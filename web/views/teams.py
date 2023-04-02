"""
This module contains Flask views for handling teams related requests.

This module defines the following views:
    `myteams()`: handles landing users' teams requests.
    `edit_team()`: handles users' specific team requests.
    `create()`: handles creating of teams requests.
    
See the views code for more detailed information on each method and its expected input and output.
"""
from web.app import app

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team
from .utils import save_image


@app.route('/myteams')
@login_required
def myteams():
    """
    Render the page for a user's teams.

    Returns:
    A rendered HTML template for the teams page, including information about the each team, its name, its location,
    and its sport.
    """
    teams = current_user.teams
    return render_template('myteams.html', teams=teams)


@app.route('/myteams/<id>', methods=['GET', 'POST'])
@login_required
def edit_team(id):
    """
    Render the page for a specific user's team.

    Args:
    id: The ID of the team to display.

    Returns:
    A rendered HTML template for the team page, including information about the team, its leader, its location,
    and its sport. If the team does not exist, the user is redirected back to the search page with an error message.
    """
    team = storage.get(Team, id)
    if request.method == 'POST':
        country_name = request.form.get('country')
        country = storage.query(Country, "name", country_name)
        if country:
            country_id = country.id
        else:
            new_country = Country(name=country_name)
            new_country.save()
            country_id = new_country.id
        
        city_name = request.form.get('city')
        city = storage.query(City, "name", city_name)
        if city:
            city_id = city.id
        else:
            new_city = City(name=city_name, country_id=country_id)
            new_city.save()
            city_id = new_city.id

        team.name = request.form.get('teamname')
        team.bio = request.form.get('teambio')
        team.city_id = city_id
        team.sport_id = request.form.get('sportid')
        reset = 'reset-picture' in request.form
        if not reset:
            image = request.files['image']
            filename = save_image(image, 'teams', team.id)
        else:
            filename = "team_default.jpg"
        if filename != "":
            team.image = filename
        team.save()
        return redirect(url_for('team_info', id=team.id))
    if (not team) or (team not in current_user.teams):
        flash("Team not found")
        return redirect(url_for('myteams'))
    sports = storage.all(Sport).values()

    edit = current_user.id == team.leader_id
    return render_template('team.html', team=team, sports=sports, edit=edit, connect=False)

@app.route('/myteams/create', methods=['GET'])
@login_required
def create():
    """
    Render the page for creation of a team.

    Returns:
    Returns a rendered HTML template for the creation of teams.
    """
    sports = storage.all(Sport).values()
    return render_template('create_teams.html', sports=sports)
