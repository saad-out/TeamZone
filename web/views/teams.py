from web.app import app

from flask import render_template
from flask_login import login_required, current_user
from models import storage, City, Country, Sport, Team


@app.route('/myteams')
@login_required
def myteams():
    teams = current_user.teams
    return render_template('myteams.html', teams=teams)


@app.route('/myteams/<id>')
@login_required
def edit_team(id):
    team = storage.get(Team, id)
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('team.html', team=team, cities=cities,countries=countries, sports=sports, edit=True)

@app.route('/myteams/create', methods=['GET', 'POST'])
@login_required
def create():
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('create_teams.html', cities=cities, countries=countries, sports=sports)
