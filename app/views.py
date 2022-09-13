from flask import render_template, flash, url_for, request, redirect
from .forms import NewPredicate
from app import app



##widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')

@app.route('/form',  methods=['GET'])
def form_page():
    form = NewPredicate()
    return render_template("formularz.html", title="", form=form)
