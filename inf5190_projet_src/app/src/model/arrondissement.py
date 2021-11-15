from app.src.db.init_db import db


class Arrondissement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)
    patinoires = db.relationship(
        "Patinoire", backref="arr_patinoire", lazy=True)
    glissades = db.relationship(
        "Glissade", backref="arr_glissade", lazy=True)
    piscines = db.relationship("Piscine", backref="arr_piscine", lazy=True)
