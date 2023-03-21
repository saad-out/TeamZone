"""
This module contains Flask views for handling main app related requests.

This module defines the following views:
    `landing_page()`: handles landing page requests.
    `dashboard()`: hadnles dashboard requests.
    `search()`: handles search & filter teams requests.
    `team_info()`: handles team info requests.
    `profile()`: hanles show user profile requests.
    
See the views code for more detailed information on each method and its expected input and output.
"""
from web.app import app

from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team, TeamInvite, GameInvite


@app.route('/')
def landing_page():
    """
    Render the landing page.

    Returns:
    A rendered HTML template for the landing page.
    """
    return render_template('index.html')


@app.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard page for authenticated users.

    Returns:
    A rendered HTML template for the dashboard page, including a list of game invitations and team invitations
    received by the user.
    """
    user_leader_teams = storage.query(Team, "leader_id", current_user.id, all=True)
    game_invitations = []
    for team in user_leader_teams:
        invites = storage.query(GameInvite, "receiver_team_id", team.id, all=True)
        game_invitations.extend(invites)
    team_invitations = storage.query(TeamInvite, "receiver_id", current_user.id, all=True)
    return render_template('dashboard.html', game_invitations=game_invitations, team_invitations=team_invitations)


@app.route('/search')
def search():
    """
    Render the search page.

    Returns:
    A rendered HTML template for the search page, including lists of teams, countries, cities, and sports.
    """
    teams = storage.all(Team).values()
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('search.html', teams=teams, countries=countries, sports=sports, cities=cities)


@app.route('/search/<id>', methods=['POST', 'GET'])
def team_info(id):
    """
    Render the page for a specific team.

    Args:
    id: The ID of the team to display.

    Returns:
    A rendered HTML template for the team page, including information about the team, its leader, its location,
    and its sport. If the team does not exist, the user is redirected back to the search page with an error message.
    """
    team = storage.get(Team, id)
    if not team:
        flash("Team doesn't exist")
        return redirect(url_for('search'))
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    edit = current_user.get_id() == team.leader_id
    return render_template('team.html', team=team, cities=cities,countries=countries, sports=sports, edit=edit)


@app.route('/profile')
@login_required
def profile():
    """
    Render the profile page for authenticated users.

    Returns:
    A rendered HTML template for the profile page, displaying the user's information.
    """
    return render_template('profile.html')


@app.route('/invites', methods=['POST'])
def invites():
    return "OK"