from app import app
from flask import render_template, redirect, request

from .procedures import get_top_worldwide, get_top_per_nationality, get_all_competitions, get_teammates
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    dk_m = get_top_per_nationality('DK', 'M')
    dk_f = get_top_per_nationality('DK', 'F')
    ww_f = get_top_worldwide('F')
    ww_m = get_top_worldwide('M')
    return render_template('index.html', dk_f=dk_f, dk_m=dk_m, ww_f=ww_f, ww_m=ww_m)


@app.route('/athletes')
def articles():
    athleteid = request.args.get('id')
    comps = get_all_competitions(athleteid)

    teams = [x['team_id'] for x in comps if x['team_id']]
    if teams:
        teammates = get_teammates(teams)

    print(teammates)

    return render_template('athletes.html', comps=comps, teammates=teammates)
