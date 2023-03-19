from web.app import app

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team
from .utils import save_image


@app.route('/myteams')
@login_required
def myteams():
    teams = current_user.teams
    return render_template('myteams.html', teams=teams)


@app.route('/myteams/<id>', methods=['GET', 'POST'])
@login_required
def edit_team(id):
    team = storage.get(Team, id)
    if request.method == 'POST':
        team.name = request.form.get('teamname')
        team.bio = request.form.get('teambio')
        #country_id = request.form.get('countryid')
        team.city_id = request.form.get('cityid')
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
    if not team:
        flash("Team not found")
        return redirect(url_for('myteams'))
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    edit = current_user.id == team.leader_id
    return render_template('team.html', team=team, cities=cities, countries=countries, sports=sports, edit=edit)

@app.route('/myteams/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == "POST":
        team_attributes = {}
        team_attributes['name'] = request.form.get('teamname')
        team_attributes['bio'] = request.form.get('teambio')
        #team_attributes['country_id'] = request.form.get('countryid')
        team_attributes['city_id'] = request.form.get('cityid')
        team_attributes['sport_id'] = request.form.get('sportid')
        team_attributes['leader_id'] = current_user.id
        sportid = request.form.get('sportid')
        team = Team(**team_attributes)
        team.players.append(current_user)
        team.save()
        return redirect(url_for('team_info', id=team.id))
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('create_teams.html', cities=cities, countries=countries, sports=sports)
