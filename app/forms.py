from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, PasswordField, validators
from wtforms.validators import DataRequired

class NewPredicate (FlaskForm):

    komorka = StringField('Komórka Organizacyjna')
    kom_orz = StringField('Komórka Zgłaszająca')
    nazwa_urz = StringField('Nazwa Urządzenia')
    typ = StringField('Typ')
    lata = IntegerField('Lata Urzydkowania')
    cena = FloatField('Cena')
    num_inw = StringField('Numer Inwentarzowy')
    producent = StringField('Producent')
    amortyzacja = StringField('Amortyzacja')
    num_fab = StringField('Numer Fabryczny')
    opis = StringField('Opis Stanu Technicznego')
    generate = SubmitField('Generuj')



