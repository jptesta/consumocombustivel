from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['secret_key'] = 'secret@@@##$)(*&¨%$#@'


db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import default
