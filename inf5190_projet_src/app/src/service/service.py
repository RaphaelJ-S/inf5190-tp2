
from app.src.db.base_donnees import Base_Donnees


class Service:

    def __init__(self, db: Base_Donnees):
        self.db = db

    def ajouter_donnees(self, donnees: list[list[str]], nom_table: str):
        if nom_table == "glissade":
            self.db.ajouter_glissades(donnees)
        elif nom_table == "patinoire":
            self.db.ajouter_patinoires(donnees)
        elif nom_table == "piscine":
            self.db.ajouter_piscines(donnees)

    def get_donnees(self, nom: str) -> list:
        return {
            "piscine": self.db.get_piscines(),
            "glissade": self.db.get_glissades(),
            "patinoire": self.db.get_patinoires()
        }.get(nom, None)
