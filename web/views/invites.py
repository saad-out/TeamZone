"""
This module contains Flask views for handling game and team invitations.

This module defines the following views:
    `game_invite()`: handles requests to send game invites.
    `update_game_invite()`: handles requests to update game invite status.
    `invite_user(team_id)`: handles requests to send team invites.
    `update_team_invite()`: handles requests to update team invite status.

See the views code for more detailed information on each method and its expected input and output.
"""
from web.app import app

from flask import render_template, request, url_for, redirect, flash, jsonify
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team, User, GameInvite, TeamInvite
from .utils import save_image, format_datetime
from datetime import datetime



@app.route('/game_invite', methods=['POST'])
@login_required
def game_invite():
    """
    Create a new game invitation between two teams.

    Method: POST
    Required Args:
        sender-team-id: ID of the team that is sending the invite.
        receiver-team-id: ID of the team that is receiving the invite.
        schedule-date: date of the game in YYYY-MM-DD format.
        schedule-time: time of the game in HH:MM format.
    Optional Args:
        request-message: a message to be included in the invitation.
    
    Returns:
        A redirect to the dashboard with a flash message indicating success or failure.
    """
    sender_team = storage.query(Team, "id", str(request.form.get('sender-team-id')))
    if not sender_team:
        flash('Something went wrong!', 'error')
        return redirect('dashboard')
    receiver_team = storage.query(Team, "id", str(request.form.get('receiver-team-id')))
    if not receiver_team:
        flash('Something went wrong!', 'error')
        return redirect('dashboard')
    
    schedule_datetime = "{}T{}".format(request.form.get('schedule-date'), request.form.get('schedule-time'))
    date = datetime.strptime(schedule_datetime, "%Y-%m-%dT%H:%M")
    message = request.form.get('request-message')

    game_attributes = {
                    "sender_team_id": sender_team.id,
                    "receiver_team_id": receiver_team.id,
                    "game_date": date,
                    "message": message
                    }
    new_game_invite = GameInvite(**game_attributes)
    new_game_invite.save()
    
    flash('Sent successfully.', 'info')
    return redirect(url_for('game', id=new_game_invite.id))


@app.route('/games/<id>')
@login_required
def game(id):
    gi = storage.get(GameInvite, id)
    if gi is None:
        flash('This game invite does not exist')
        return redirect(url_for('dashboard'))
    sender_team = gi.sender_team
    receiver_team = gi.receiver_team
    
    return render_template('game.html', gi=gi, sender_team=sender_team, receiver_team=receiver_team, format_datetime=format_datetime)

@app.route('/update_game_invite', methods=['POST'])
@login_required
def update_game_invite():
    """
    Update an existing game invitation with the given ID.

    Method: POST
    Required JSON Args:
        invitation_id: ID of the invitation to update.
        action: 'accept' or 'decline'.
    
    Returns:
        A JSON response indicating success or failure.
    """
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    else:
        invite_data = request.get_json()
    
    game_invite = storage.query(GameInvite, "id", invite_data.get('invitation_id'))
    if not game_invite:
        return jsonify({"error": "Not found"}), 404
    if invite_data.get('action') not in ['accept', 'decline']:
        return jsonify({"error": "Invalid status"}), 400
        
    if invite_data.get('action') == 'accept':
        game_invite.status = 'accepted'
    else:
        game_invite.status = 'declined'
    game_invite.save()

    return jsonify({})


@app.route('/invite_user/<team_id>', methods=['POST'])
@login_required
def invite_user(team_id):
    """
    Invite a user to join the team with the given ID.

    Method: POST
    Required Args:
        username: the username of the user to invite.
        request-message: a message to be included in the invitation.
    
    Returns:
        A redirect to the team info page with a flash message indicating success or failure.
    """
    user = storage.query(User, "username", request.form.get('username'))
    if not user:
        flash('Username does not exist!', 'error')
        return redirect('/myteams/{}'.format(team_id))
    team = storage.query(Team, "id", team_id)
    if not team:
        flash('Something went wrong!', 'error')
        return redirect(url_for('dashboard'))
    message = request.form.get('request-message')
    
    new_team_invite = TeamInvite(sender_id=team.leader.id, receiver_id=user.id, team_id=team.id, message=message)
    new_team_invite.save()

    flash('Sent successfully.', 'message')
    return redirect('/myteams/{}'.format(team_id))


@app.route('/update_team_invite', methods=['POST'])
@login_required
def update_team_invite():
    """
    Update an existing team invitation with the given ID.

    Method: POST
    Required JSON Args:
        invitation_id: ID of the invitation to update.
        action: 'accept' or 'decline'.
    
    Returns:
        A JSON response indicating success or failure.
    """
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    else:
        invite_data = request.get_json()

    team_invite = storage.query(TeamInvite, "id", invite_data.get('invitation_id'))
    if not team_invite:
        return jsonify({"error": "Not found"}), 404
    if invite_data.get('action') not in ['accept', 'decline']:
        return jsonify({"error": "Invalid status"}), 400
        
    if invite_data.get('action') == 'accept':
        team_invite.status = 'accepted'
        team = storage.query(Team, "id", team_invite.team_id)
        if not team:
            flash('Something went wrong!', 'error')
            return redirect(url_for('dashboard'))
        new_player = storage.query(User, "id", team_invite.receiver_id)
        if not new_player:
            flash('Something went wrong!', 'error')
            return redirect(url_for('dashboard'))
        
        print(new_player.teams)

        team.players.append(new_player)
        team.save()
        
        print(new_player.teams)
        print(team.players)
    else:
        team_invite.status = 'declined'
    team_invite.save()

    return jsonify({})