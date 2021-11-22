from app.src.db.init_db import db


class Patinoire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    date_heure = db.Column(db.String(20), nullable=False)
    deblaye = db.Column(db.String(1), nullable=False)
    arrose = db.Column(db.String(1), nullable=False)
    resurface = db.Column(db.String(1), nullable=False)
    nom_arr = db.Column(db.String(50), db.ForeignKey(
        "arrondissement.nom", ondelete="CASCADE"),
        nullable=True, default="N/A")

    def as_partial_list(self):
        return [self.date_heure, self.deblaye, self.nom, self.arrose,
                self.resurface, self.nom_arr]
