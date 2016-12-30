from flask import abort
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app import app
from app import get_db
from app import forms


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lastten')
def lastten():
    db = get_db()
    feedings = db.feedings
    all_feedings = list(feedings.find())[-10:]
    diap = db.bathroom
    all_changes = list(diap.find())[-10:]
    return render_template('last_ten.html', feed=all_feedings, diap=all_changes)


@app.route('/feeding', methods=['GET', 'POST'])
def feeding():
    form = forms.FeedingForm()
    if request.method == 'POST' and form.validate():
        doc = {}
        db = get_db()
        doc['side'] = form.side.data
        doc['time'] = form.time.data
        db.feedings.insert(doc)
        return redirect(url_for('index'))
    return render_template('add_form.html', form=form, title='Add a feeding', action=url_for('feeding'))


@app.route('/diaper', methods=['GET', 'POST'])
def diaper():
    form = forms.DiaperForm()
    if request.method == 'POST' and form.validate():
        doc = {}
        db = get_db()
        doc['time'] = form.time.data
        doc['type'] = form.diaper_type.data
        db.bathroom.insert(doc)
        return redirect(url_for('index'))
    return render_template('add_form.html', form=form, title='Add a diaper change', action=url_for('diaper'))


@app.route('/allfeedings')
def all_feedings():
    db = get_db()
    all_feed = db.feedings.find()
    return render_template('table.html', entries=all_feed, title='Feedings', headings=['Time', 'Breast used'],
                            keys=['time', 'side'])


@app.route('/alldiapers')
def all_diapers():
    db = get_db()
    all_diapers = db.bathroom.find()
    return render_template('table.html', entries=all_diapers, title='Diaper changes', headings=['Time', 'Type'],
                            keys=['time', 'type'])
