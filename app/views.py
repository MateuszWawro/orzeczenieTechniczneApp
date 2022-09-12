from flask import render_template, flash, url_for, request, redirect
from app import app
from .forms import NewPredicate



##widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')
@app.route('/form')
def form_page():
    return render_template("formularz.html",title="")
