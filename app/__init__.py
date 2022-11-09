from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from contextlib import suppress
from flask_login import LoginManager

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\Mateusz-DELL\\PycharmProjects\\orzeczenieTechniczneApp\\orztechApp_database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\mwawro\\PycharmProjects\\orzeczenieTechniczneApp\\orztechApp_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'the random string'



lm = LoginManager(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from . import views, forms