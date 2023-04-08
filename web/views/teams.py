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


@app.route('/myteams/<id>', methods=['GET'])
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
    if (not team) or (team not in current_user.teams):
        flash("Team not found")
        return redirect(url_for('myteams'))
    
    sports = storage.all(Sport).values()
    edit = current_user.id == team.leader_id
    return render_template('team.html', team=team, sports=sports, edit=edit, connect=False)


@app.route('/myteams/<id>/image', methods=['POST'])
@login_required
def store_team_image(id):
    """
    Store the image for a specific team.

    Args:
    id: The ID of the team to store the image for.

    Returns:
    Image filename.
    """
    from flask import jsonify

    team = storage.get(Team, id)
    if not team:
        return jsonify({'error': 'Team not found'}), 404
    
    image = request.files['image']
    filename = save_image(image, 'teams', team.id)
    return jsonify({'filename': filename})
    


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
