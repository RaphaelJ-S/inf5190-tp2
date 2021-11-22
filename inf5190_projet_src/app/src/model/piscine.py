from app.src.db.init_db import db


class Piscine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_uev = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(50), nullable=False)
    nom = db.Column(db.String(50), nullable=False)
    adresse = db.Column(db.String(80), nullable=False)
    propriete = db.Column(db.String(50))
    gestion = db.Column(db.String(50))
    point_x = db.Column(db.String(15), nullable=False)
    point_y = db.Column(db.String(15), nullable=False)
    equipement = db.Column(db.String(50))
    longitude = db.Column(db.String(15), nullable=False)
    latitude = db.Column(db.String(15), nullable=False)
    nom_arr = db.Column(db.String(50), db.ForeignKey(
        "arrondissement.nom", ondelete="CASCADE"),
        nullable=True, default="N/A")

    def as_partial_list(self):
        return [self.id_uev, self.type, self.nom, self.adresse, self.propriete,
                self.gestion, self.point_x, self.point_y, self.equipement,
                self.longitude, self.latitude, self.nom_arr]
