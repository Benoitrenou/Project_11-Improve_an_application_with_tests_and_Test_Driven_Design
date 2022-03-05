import json
import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']


def loadCompetitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()

@app.route('/')
def index():
    return render_template('index.html', clubs=clubs)

@app.route('/showSummary',methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html',club=club,competitions=competitions)
    except IndexError:
        flash('Email not found - Please try again')
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        date_competition = datetime.datetime.strptime(
            foundCompetition['date'],
            "%Y-%m-%d %H:%M:%S"
            )
        date_today = datetime.datetime.now()
        if date_today > date_competition:
            flash('Sorry, this competition already took place - Select an other competition')
            return render_template('welcome.html', club=foundClub, competitions=competitions)
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces',methods=['POST'])
def purchasePlaces():
    maximum_places = 12
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired <= 0:
        flash('Sorry, you must choose a positive number of places - Try again')
        return render_template('booking.html',club=club,competition=competition)
    if placesRequired > maximum_places:
        flash('Sorry, you only can book 12 places maximum - Try again')
        return render_template('booking.html',club=club,competition=competition)
    if int(club['points']) < placesRequired:
        flash('Sorry, you required more places than possible - Try again')
        return render_template('booking.html',club=club,competition=competition)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
    club['points'] = int(club['points']) - placesRequired
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/points_display')
def points_display():
    return render_template('points_display.html', clubs=clubs, competitions=competitions)



@app.route('/logout')
def logout():
    return redirect(url_for('index'))