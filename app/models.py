from . import db
from sqlalchemy import String
from flask_login import UserMixin

#model bazy danych użytkowników
class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(15))
    password = db.Column(db.String(32), nullable=False)
    name = db.Column(db.String(15))
    surname = db.Column(db.String(15))


#model bazy danych orzeczeń
class Orzeczenie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kom_orz = db.Column(db.String())
    komorka = db.Column(db.String())
    nazwa_urz = db.Column(db.String())
    typ = db.Column(db.String())
    rok = db.Column(db.Integer)
    lata = db.Column(db.String())
    cena = db.Column(db.String())
    num_inw = db.Column(db.String())
    producent = db.Column(db.String())
    amortyzacja = db.Column(db.String())
    num_fab = db.Column(db.String())
    opis = db.Column(db.String())