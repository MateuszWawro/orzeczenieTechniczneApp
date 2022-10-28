from flask import render_template, flash, url_for, request, redirect
from .forms import NewPredicate
from app import app
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

