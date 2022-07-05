from flask import Flask
from sqlalchemy import SQLAlchemy




app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///base.db'
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://{root}:{}@{localhost}/testadb".format(username, password, server)
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://username:password@server/db"

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/testadb'
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


#app.config['secret_key'] = 'secret@@@##$)(*&¨%$#@'

#db = SQLAlchemy(app)

from app.controllers import default