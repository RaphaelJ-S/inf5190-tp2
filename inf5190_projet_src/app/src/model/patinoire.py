from app.src.db.init_db import db


class Patinoire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    date_heure = db.Column(db.String(20), nullable=False)
    deplaye = db.Column(db.String(1), nullable=False)
    arrose = db.Column(db.String(1), nullable=False)
    resurface = db.Column(db.String(1), nullable=False)
    arrondissement = db.Column(db.String(50), db.ForeignKey(
        "arr_patinoire.nom"), nullable=True, default="Montréal")
