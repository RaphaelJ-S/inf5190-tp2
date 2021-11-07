from app.src.app import db
db.create_all()


class Piscine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_uev = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    arrondissement = db.Column(db.String(80), nullable=False)
    adresse = db.Column(db.String(80), nullable=False)
    propriete = db.Column(db.String(50))
    gestion = db.Column(db.String(50))
    point_x = db.Column(db.Float(4), nullable=False)
    point_y = db.Column(db.Integer, nullable=False)
    equipement = db.Column(db.String(50))
    longitude = db.Column(db.Float(6), nullable=False)
    latitude = db.Column(db.Float(6), nullable=False)
