from app import db


class Consumo(db.Model):
    __tablename__ = 'consumo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Data = db.Column(db.DateTime)
    Km = db.Column(db.Float)
    Tanque = db.Column(db.Float)
    Valorporlitro = db.Column(db.Float)
    KmTotal = db.Column(db.Float)
    Media = db.Column(db.Float)
    Totalgasolina = db.Column(db.Float)
    Cidadeestrada = db.Column(db.String(50))
    Posto = db.Column(db.String(50))
    tipo = db.Column(db.String(10))
    vlrkm = db.Column(db.Float)


class Veiculo(db.Model):
    __tablename__= 'veiculo'
    idveiculo = db.Column(db.Integer, primary_key+True, autoincrement=True)
    Marca = db.Column(db.String(50))
    Modelo = db.Column(db.String(50))

