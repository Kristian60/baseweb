from app import app
from flask import render_template, redirect
from .forms import SampleForm

from .procedures import get_top_worldwide, get_top_per_nationality
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    dk_m = get_top_per_nationality('DK', 'M')
    dk_f = get_top_per_nationality('DK', 'F')
    ww_f = get_top_worldwide('F')
    ww_m = get_top_worldwide('M')
    return render_template('index.html', dk_f=dk_f, dk_m=dk_m, ww_f=ww_f, ww_m=ww_m)


@app.route('/articles')
def articles():
    return render_template('articles.html')


@app.route('/forms', methods=['GET', 'POST'])
def forms():
    form = SampleForm()

    # If form is upon submission and is validated success
    if form.validate_on_submit():
        return redirect('index')

    return render_template('forms.html', form=form)
