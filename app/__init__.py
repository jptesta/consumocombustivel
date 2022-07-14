from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///base.db'

app.config['secret_key'] = 'secret@@@##$)(*&¨%$#@'

db = SQLAlchemy(app)

from app.controllers import default
