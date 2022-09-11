from flask import render_template, flash, url_for, request, redirect
from app import app


##widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')



