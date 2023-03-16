from web.app import app

from flask import render_template
from flask_login import login_required
from models import storage, City, Country, Sport, Team


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/search')
def search():
    teams = storage.all(Team).values()
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('search.html', teams=teams, countries=countries, sports=sports, cities=cities)


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('create_teams.html', cities=cities, countries=countries, sports=sports)


@app.route('/edit')
@login_required
def edit():
    teams = storage.all(Team).values()
    return render_template('teams.html', teams=teams)


@app.route('/teams/<id>')
def edit_team(id):
    team = storage.get(Team, id)
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('team.html', team=team, cities=cities, countries=countries, sports=sports)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')