from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, PasswordField, validators


class NewPredicate (FlaskForm):
    komorka = StringField('Komórka Organizacyjna',[validators.DataRequired()])
    kom_orz = StringField('Komórka Zgłaszająca',[validators.DataRequired()])
    nazwa_urz = StringField('Nazwa Urządzenia',[validators.DataRequired()])
    typ = StringField('Typ')
    lata = IntegerField('Lata Urzydkowania')
    cena = FloatField('Cena',[validators.DataRequired()])
    num_inw = StringField('Numer Inwentarzowy',[validators.DataRequired()])
    producent = StringField('Producent',[validators.DataRequired()])
    amortyzacja = StringField('Amortyzacja',[validators.DataRequired()])
    num_fab = StringField('Numer Fabryczny')
    opis = StringField('Opis Stanu Technicznego',[validators.DataRequired()])
    generate = SubmitField('Generuj')



