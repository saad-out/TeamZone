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

from flask import render_template, redirect, flash, url_for, g
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team, TeamInvite, GameInvite
from .utils import format_datetime


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
    sent & received by the user.
    """
    current_leader_teams = [team for team in current_user.teams if current_user.id == team.leader_id]
    sent_team_invitations = storage.query(TeamInvite, "sender_id", current_user.id, all=True)
    received_team_invitations = storage.query(TeamInvite, "receiver_id", current_user.id, all=True)

    answered_team_invitations = []
    pending_team_invitations = []
    if sent_team_invitations:
        answered_team_invitations += [invite for invite in sent_team_invitations if invite.status in ['accepted', 'declined']]
    if received_team_invitations:
        pending_team_invitations += [invite for invite in received_team_invitations if invite.status == 'pending']

    answered_game_invitations = []
    pending_game_invitations = []
    for team in current_leader_teams:
        sent_invites = storage.query(GameInvite, "sender_team_id", team.id, all=True)
        if sent_invites:
            answered_game_invitations += [invite for invite in sent_invites if invite.status in ['accepted', 'declined']]
        received_invites = storage.query(GameInvite, "receiver_team_id", team.id, all=True)
        if received_invites:
            pending_game_invitations += [invite for invite in received_invites if invite.status == 'pending']

    g.invites = answered_game_invitations + answered_team_invitations
    return render_template('dashboard.html',
                           game_invitations=pending_game_invitations,
                           team_invitations=pending_team_invitations,
                           game_notifications=answered_game_invitations,
                           team_notifications=answered_team_invitations,
                           format_datetime=format_datetime)


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

    if not current_user.is_authenticated:
        edit = False
        connect = True
    else:
        edit = current_user.get_id() == team.leader_id
        connect = team not in current_user.teams
        if not connect:
            flash("You are already a member of this team")
            return redirect(url_for('edit_team', id=team.id))

    return render_template('team.html', team=team, sports=sports, edit=edit, connect=connect)


@app.route('/profile')
@login_required
def profile():
    """
    Render the profile page for authenticated users.

    Returns:
    A rendered HTML template for the profile page, displaying the user's information.
    """
    return render_template('profile.html')