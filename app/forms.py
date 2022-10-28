from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField, PasswordField, validators, DecimalField, TextAreaField

#klasa formularza orzeczenia
class NewPredicate (FlaskForm):
    numer_wniosku = StringField('Numer Wniosku')
    kom_orz = StringField('Komórka Organizacyjna',[validators.DataRequired()])
    komorka = StringField('Komórka Zgłaszająca',[validators.DataRequired()])
    nazwa_urz = StringField('Nazwa Urządzenia',[validators.DataRequired()])
    typ = StringField('Typ')
    rok = DecimalField('Rok Produkcji')
    lata = IntegerField('Lata Urzydkowania')
    cena = FloatField('Cena',[validators.DataRequired()])
    num_inw = StringField('Numer Inwentarzowy',[validators.DataRequired()])
    producent = StringField('Producent',[validators.DataRequired()])
    amortyzacja = StringField('Amortyzacja',[validators.DataRequired()])
    num_fab = StringField('Numer Fabryczny')
    opis = TextAreaField('Opis Stanu Technicznego',[validators.DataRequired()])
    generate = SubmitField('Generuj')

#klasa formularza logowania
class LoginForm(FlaskForm):
    login = StringField('Login', [validators.DataRequired()])
    password = PasswordField('Hasło',[validators.DataRequired()])
    submit = SubmitField('Zaloguj')


