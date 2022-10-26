from flask import render_template, flash, url_for, request, redirect
from .forms import NewPredicate
from app import app
from .pdf import create_report


##widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')

@app.route('/form',  methods=['GET','POST'])
def form_page():
    form = NewPredicate()
    if form.validate_on_submit():
        create_report(form=form)
        return redirect('/')
    else:
        print(form.errors)
    return render_template("formularz.html", title="", form=form)

