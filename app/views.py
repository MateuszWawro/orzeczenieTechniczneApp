from flask import render_template, flash, url_for, request, redirect
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy.exc import DBAPIError
from .forms import NewPredicate, LoginForm, AwariaForm
from .models import User, Orzeczenie, Awaria
from app import app, db, lm
from .report_generate import create_report, generate_report
from .report_generate_awar import create_awaria_rep, generate_report_sec
from flask import send_file
import datetime
from passlib.hash import bcrypt_sha256
from sqlalchemy import func


#widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')


#generowanie raportu i dodanie do bazy danych
@login_required
@app.route('/form',  methods=['GET','POST'])
def form_page():
    form = NewPredicate()
    o = Orzeczenie.query.all()
    z = list()
    for i in o:
        z.append(i.id)
    z.sort()
    max_nr_orz = [int(x) for x in z[-1:]]
    form.numer_wniosku.data = max_nr_orz[0]+1
    if form.validate_on_submit():
        try:
            q = Orzeczenie(id=form.numer_wniosku.data, kom_orz=form.kom_orz.data, komorka=form.komorka.data,
                       nazwa_urz=form.nazwa_urz.data, typ=form.typ.data, rok=form.rok.data, lata=form.lata.data,
                       cena=form.cena.data, num_inw=form.num_inw.data, producent=form.producent.data,
                       amortyzacja=form.amortyzacja.data,
                       num_fab=form.num_fab.data, opis=form.opis.data)
            db.session.add(q)
        except DBAPIError as e:
            flash(e.detail)
            db.session.rollback()
        else:
            db.session.commit()
            return send_file(create_report(form=form), download_name='{0}#{3}_{1}_{2}.xlsx'.format(form.numer_wniosku.data, form.nazwa_urz.data, str(form.num_inw.data).replace('/', '#'), datetime.date.today().year), as_attachment=True,
                         mimetype='application/vnd.ms-excel')
    else:
        flash(form.errors)
    return render_template("formularz.html", title="", form=form)


#formularz logowania
@app.route('/login', methods =['GET', 'POST'])
def view_login():
    form = LoginForm()
    if form.validate_on_submit():
        login = User.query.filter_by(login=form.login.data).first()
        print(login)
        if login and bcrypt_sha256.verify(form.password.data, login.password):
            print('1')
            login_user(login)
            print(current_user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('form_page'))
        flash('złe hasło lub login')
        return redirect(url_for('home_page'))
    return render_template("login_form.html", title="", form=form)


@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#wylogowywanie
@login_required
@app.route('/logout')
def view_logout():
    logout_user()
    return redirect(url_for('home_page'))


#lista orzeczeń
@login_required
@app.route('/lista_orz')
def view_lista():
    lista_orzecz = Orzeczenie.query.all()
    return render_template("lista_orzeczen.html", title="Lista Orzeczeń - zalogowano jako:{0}".format(current_user.name), lista_orzecz=lista_orzecz)

#lista protokołów
@login_required
@app.route('/lista_prot')
def view_lista_sec():
    lista_prot = Awaria.query.all()
    return render_template("lista_orzeczen_awar.html", title="Lista Protokołów Awaryjnych - zalogowano jako:{0}".format(current_user.name), lista_prot=lista_prot)


#generacja/podglad z listy
@login_required
@app.route("/generate/<int:id>", methods=["POST", "GET"])
def view_generate(id):
    lista_orzecz = Orzeczenie.query.filter_by(id=id).first()
    return send_file(generate_report(lista_query=lista_orzecz),
                     download_name='{0}#{3}_{1}_{2}.xlsx'.format(lista_orzecz.id, lista_orzecz.nazwa_urz,
                                                                 str(lista_orzecz.num_inw).replace('/', '#'),
                                                                 datetime.date.today().year), as_attachment=True,
                     mimetype='application/vnd.ms-excel')


#generacja/podglad z listy awaryjny protokol
@login_required
@app.route("/generate_sec/<int:id>", methods=["POST", "GET"])
def view_generate_sec(id):
    lista_prot = Awaria.query.filter_by(id=id).first()
    return send_file(generate_report_sec(lista_query_sec=lista_prot),
                     download_name='{0}_{1}.xlsx'.format(lista_prot.urzadz_miejsc, datetime.date.today()), as_attachment=True, mimetype='application/vnd.ms-excel')


#formularz logowania 2
@app.route('/login_sec', methods =['GET', 'POST'])
def view_login_sec():
    form = LoginForm()
    if form.validate_on_submit():
        login = User.query.filter_by(login=form.login.data).first()
        print(login)
        if login and bcrypt_sha256.verify(form.password.data, login.password):
            print('1')
            login_user(login)
            print(current_user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('form_page_sec'))
        flash('złe hasło lub login')
        return redirect(url_for('home_page'))
    return render_template("login_form.html", title="", form=form)

#generowanie raportu i dodanie do bazy danych
@login_required
@app.route('/form_sec',  methods=['GET', 'POST'])
def form_page_sec():
    awaria_form = AwariaForm()
    if awaria_form.validate_on_submit():
        try:
            q = Awaria(urzadz_miejsc=awaria_form.urzadz_miejsc.data, opis=awaria_form.opis_awa.data,
                       straty=awaria_form.straty.data, zalecenia=awaria_form.zalecenia.data, koszt_szac=awaria_form.koszt_szac.data,
                       cz_1_kom=awaria_form.czlonek_1.data,
                       cz_2_kom=awaria_form.czlonek_2.data, stanowisko=awaria_form.stanowisko_1.data, stanowisko2=awaria_form.stanowisko_2.data)
            db.session.add(q)
        except DBAPIError as e:
            flash(e.detail)
            db.session.rollback()
        else:
            db.session.commit()
            return send_file(create_awaria_rep(awaria_form=awaria_form), download_name='{0}_{1}.xlsx'.format(awaria_form.urzadz_miejsc.data, datetime.date.today()), as_attachment=True, mimetype='application/vnd.ms-excel')
    else:
        flash(awaria_form.errors)
    return render_template("formularz_awar.html", title="", awaria_form=awaria_form)


