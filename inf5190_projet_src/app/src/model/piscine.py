from app.src.db.init_db import db


class Piscine(db.Model):
    """
    Représentation d'une piscine
    """
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

    def as_partial_list(self) -> list:
        """
        Retourne une liste partielle des attributs de la piscine.
        """
        return [self.id_uev, self.type, self.nom, self.adresse, self.propriete,
                self.gestion, self.point_x, self.point_y, self.equipement,
                self.longitude, self.latitude, self.nom_arr]

    def as_dict(self) -> dict:
        """
        Retourne tous les attributs de la piscine sous forme de dictionnaire.
        """
        return {
            "id": self.id,
            "id_uev": self.id_uev,
            "type": self.type,
            "nom": self.nom,
            "adresse": self.adresse,
            "propriete": self.propriete,
            "gestion": self.gestion,
            "point_x": self.point_x,
            "point_y": self.point_y,
            "equipement": self.equipement,
            "longitude": self.longitude,
            "latitude": self.latitude,
            "nom_arr": self.nom_arr
        }

    def __str__(self) -> str:
        return f"Piscine {self.nom} - Arrondissement {self.nom_arr}."
