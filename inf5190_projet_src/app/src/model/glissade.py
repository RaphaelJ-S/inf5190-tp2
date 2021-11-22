from app.src.db.init_db import db


class Glissade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    ouvert = db.Column(db.String(1), nullable=False)
    deblaye = db.Column(db.String(1), nullable=False)
    cle = db.Column(db.String(10), nullable=False)
    date_maj = db.Column(db.String(30), nullable=False)
    nom_arr = db.Column(db.String(50), db.ForeignKey(
        "arrondissement.nom", ondelete="CASCADE"),
        nullable=True, default="N/A")

    def as_partial_list(self) -> list[str]:
        return [self.ouvert, self.deblaye, self.nom, self.cle, self.date_maj,
                self.nom_arr]
