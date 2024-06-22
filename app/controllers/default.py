from flask import render_template, request

from app.models import tables
from app.models.tables import Consumo
from app import app, db


@app.route('/')
def index():
    consumo = tables.Consumo.query.all()
    return render_template('index.html', consumo=consumo)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        dataabastecimento = request.form['dataabastecimento']
        vlrpl = request.form['vlrpl']
        km = request.form['km']
        tanque = request.form['tanque']
        media = request.form['media']
        totalcombustivel = request.form['totalcombustivel']
        cidadeouestrada = request.form['cidadeouestrada']
        posto = request.form['posto']
        tipo = request.form['tipo']
        vlrkm = request.form['vlrpkm']
        consumo = Consumo(Data=dataabastecimento, Valorporlitro=vlrpl, Km=km, Tanque=tanque, Media=media, Totalcombustivel=totalcombustivel, Cidadeouestrada=cidadeouestrada, Posto=posto, Tipo=tipo, Vlrkm=vlrkm)
        db.session.add(consumo)
        db.session.commit()
    return render_template('cadastrar.html', consumo=consumo)
