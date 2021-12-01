
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

    def get_installations(self, arrondissement: str) -> list:
        nom_arrondissements = [arrondissement.nom
                               for arrondissement
                               in self.db.get_arrondissements()]
        if arrondissement is None:
            raise TypeError(
                "Vous devez fournir le paramètre 'arrondissement'.")
        elif not arrondissement in nom_arrondissements:
            pres_nom = ', '.join(nom_arrondissements)
            raise ValueError(f"L'arrondissement que vous avec fourni n'est" +
                             " pas valide. Veuillez entrer une des options " +
                             "suivantes : " + pres_nom)
        else:
            patinoires, piscines, glissades = (
                self.db.
                get_installations_avec_arrondissement(arrondissement))
            installations = {
                "piscines": [pisc[1].as_dict() for pisc in piscines],
                "patinoires": [pat[1].as_dict() for pat in patinoires],
                "glissades": [glis[1].as_dict() for glis in glissades]
            }
            return installations
