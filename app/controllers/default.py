from flask import render_template, request

from app.models import tables
from app.models.tables import Consumo
from app import app, db


@app.route('/', methods=['GET', 'POST'])
def index():
    consumo = tables.Consumo.query.all()
    if request.method == 'POST':
        data = request.method['data']
        vlrpl = request.method['vlrpl']
        km = request.method['km']
        tanque = request.method['tanque']
        media = request.method['media']
        totalcombustivel = request.method['totalcombustivel']
        cidadeouestrada = request.method['cidadeouestrada']
        posto = request.method['posto']
        tipo = request.method['tipo']
        vlrpkm = request.method['vlrpkm']
        consumo = Consumo(Data=data, Vlrpl=vlrpl, Km=km, Tanque=tanque, Media=media,Totalcombustivel=totalcombustivel,
                          Cidadeouestrada=cidadeouestrada, Posto=posto, Tipo=tipo, Vlrpkm=vlrpkm)
        db.session.add(consumo)
        db.session.commit()
    return render_template('index.html', consumo=consumo)
