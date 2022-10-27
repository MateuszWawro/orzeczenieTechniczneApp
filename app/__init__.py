from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

app.secret_key = 'the random string'


csrf = CSRFProtect(app)

from . import views, forms