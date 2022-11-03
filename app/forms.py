from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, PasswordField, validators, DecimalField, TextAreaField


#klasa formularza orzeczenia
class NewPredicate (FlaskForm):
    numer_wniosku = IntegerField('Numer Wniosku')
    kom_orz = StringField('Komórka Organizacyjna',[validators.DataRequired()])
    komorka = StringField('Komórka Zgłaszająca',[validators.DataRequired()])
    nazwa_urz = StringField('Nazwa Urządzenia',[validators.DataRequired()])
    typ = StringField('Typ')
    rok = IntegerField('Rok Produkcji')
    lata = StringField('Lata Urzydkowania')
    cena = StringField('Cena',[validators.DataRequired()])
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


#klasa formularza protokołu
class AwariaForm(FlaskForm):
    urzadz_miejsc = StringField()
    opis_awa = TextAreaField()
    straty = StringField()
    zalecenia = StringField()
    koszt_szac = StringField()
    czlonek_1 = StringField()
    czlonek_2 = StringField()
    stanowisko_1 = SelectField('Wybierz stanowisko',
                               choices=[('1','Kierownik'),('2','Z-ca kierownika'),
                                        ('3','Starszy Informatyk'),('4','Informatyk')])
    stanowisko_2 = SelectField('Wybierz stanowisko',
                               choices=[('kierownik','Kierownik'),('z-ca kierownika','Z-ca kierownika'),
                                        ('starszy informatyk','Starszy Informatyk'),('informatyk','Informatyk')])
    generate = SubmitField('Generuj')