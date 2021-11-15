from re import A
from app.src.db.init_db import db


class Glissade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    ouvert = db.Column(db.String(1), nullable=False)
    deblaye = db.Column(db.String(1), nullable=False)
    cle = db.Column(db.String(10), nullable=False)
    date_maj = db.Column(db.String(30), nullable=False)
    arrondissement = db.Column(db.String(50), db.ForeignKey(
        "arr_glissade.nom"), nullable=True, default="Montréal")
