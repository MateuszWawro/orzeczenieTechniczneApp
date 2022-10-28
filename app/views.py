from flask import render_template, flash, url_for, request, redirect
from flask_login import login_user, logout_user
from sqlalchemy.exc import DBAPIError
from .forms import NewPredicate, LoginForm
from .models import User
from app import app, db, lm
from .report_generate import create_report
from flask import send_file
import datetime


#widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')

#generowanie raportu
@app.route('/form',  methods=['GET','POST'])
def form_page():
    form = NewPredicate()
    if form.validate_on_submit():
       return send_file(create_report(form=form), download_name='{0}#{3}_{1}_{2}.xlsx'.format(form.numer_wniosku.data, form.nazwa_urz.data, str(form.num_inw.data).replace('/', '#'), datetime.date.today().year), as_attachment=True,
                         mimetype='application/vnd.ms-excel')
    else:
        print(form.errors)
    return render_template("formularz.html", title="", form=form)

#formularz logowania
@app.route('/login', methods =['GET,', 'POST'])
def view_login():
    form = LoginForm()
    if form.validate_on_submit():
        login = User.query.filterby(login=form.login.data).first()
        if login and login.password == form.password.data:
            login_user(login)
            next_page = request.args.get('next')
            return  redirect(next_page or url_for('form_page'))
        flash('złe hasło lub login')
        return redirect(url_for('/'))
    return render_template("formularz.html", title="", form=form)

@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#wylogowywanie
@app.route('/logout')
def view_logout():
    logout_user()
    return redirect(url_for('/'))