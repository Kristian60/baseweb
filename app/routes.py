from app import app
from flask import render_template, redirect, request
from .procedures import get_top_worldwide, get_top_per_nationality, get_all_competitions, get_teammates, get_athlete_info

dk_m = get_top_per_nationality('DK', 'M')
dk_f = get_top_per_nationality('DK', 'F')
ww_f = get_top_worldwide('F')
ww_m = get_top_worldwide('M')

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    tables = [ww_m, ww_f, dk_m, dk_f]
    return render_template('index.html',
                           tables=tables,
                           zip=zip,
                           cols=['World Top 10 Men','World Top 10 Women',
                                 'Denmark Top 10 Men','Denmark Top 10 Women'])

@app.route('/athlete')
def athlete():
    athleteid = request.args.get('id')

    athlete_info = get_athlete_info(athleteid)[0]
    comps = get_all_competitions(athleteid)

    teams = [x['team_id'] for x in comps if x['team_id']]
    if teams:
        teammates = get_teammates(teams)
    else:
        teammates = None

    return render_template('athlete.html', comps=comps, teammates=teammates, athlete_info=athlete_info)

@app.route('/competition')
def competition():
    comp_id = request.args.get('id')

    return render_template('competition.html')
