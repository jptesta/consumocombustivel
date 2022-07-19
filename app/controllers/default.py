from flask import render_template

from app.models import tables
from app import app


@app.route('/')
def index():
    consumo = tables.Consumo.query.all()
    return render_template('index.html', consumo=consumo)
