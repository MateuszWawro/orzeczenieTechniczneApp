from flask import render_template, flash, url_for, request, redirect
from .forms import NewPredicate
from app import app
from .report_generate import create_report
from flask import send_file



#widok strony głównej
@app.route('/')
def home_page():
    return render_template("index.html", title='')

#generowanie raportu
@app.route('/form',  methods=['GET','POST'])
def form_page():
    form = NewPredicate()
    if form.validate_on_submit():
        return send_file(create_report(form=form), download_name='orzeczenie.xlsx', as_attachment=True,
                         mimetype='application/vnd.ms-excel')
    else:
        print(form.errors)
    return render_template("formularz.html", title="", form=form)

