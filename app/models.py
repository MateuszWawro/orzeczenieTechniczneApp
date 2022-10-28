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