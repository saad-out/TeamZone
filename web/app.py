from flask import Flask, render_template
from models import storage, City, Country, Sport, Team

app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/search')
def search():
    teams = storage.all(Team).values()
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('search.html', teams=teams, countries=countries, sports=sports, cities=cities)


@app.route('/create', methods=['GET', 'POST'])
def create():
    cities = storage.all(City).values()
    countries = storage.all(Country).values()
    sports = storage.all(Sport).values()
    return render_template('create_teams.html', cities=cities, countries=countries, sports=sports)


@app.route('/edit')
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
def profile():
    return render_template('profile.html')


@app.route('/signout')
def signout():
    return render_template('signout.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)