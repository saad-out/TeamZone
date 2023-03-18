from web.app import app

from flask import render_template, redirect, flash, url_for
from flask_login import login_required, current_user
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


@app.route('/search/<id>', methods=['POST', 'GET'])
def team_info(id):
    team = storage.get(Team, id)
    if not team:
        flash("Team doesn't exist")
        return redirect(url_for('search'))
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    edit = current_user.id == team.leader_id
    return render_template('team.html', team=team, cities=cities,countries=countries, sports=sports, edit=edit)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')