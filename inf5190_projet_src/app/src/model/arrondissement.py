from app.src.db.init_db import db


class Arrondissement(db.Model):
    """
    Représentation d'un arrondissement.
    """
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), unique=True, nullable=False)
    patinoires = db.relationship(
        "Patinoire", backref="nom_arr_pat", cascade="all, delete",
        passive_deletes=True, lazy=True)
    glissades = db.relationship(
        "Glissade", backref="nom_arr_gliss", cascade="all, delete",
        passive_deletes=True, lazy=True)
    piscines = db.relationship(
        "Piscine", backref="nom_arr_pisc", cascade="all, delete",
        passive_deletes=True, lazy=True)

    def as_dict(self):
        """
        Retourne l'id et le nom de l'arrondissement sous forme de dictionnaire id:X, nom:Y
        """
        return {
            "id": self.id,
            "nom": self.nom
        }
