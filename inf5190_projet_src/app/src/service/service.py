
from app.src.db.base_donnees import Base_Donnees


class Service:
    """
    Couche d'abstraction entre le contrôleur et la base de données
    contenant la logique d'affaire.
    """

    def __init__(self, db: Base_Donnees):
        self.db = db

    def get_noms_arrondissements(self) -> list[str]:
        """
        Retourne les noms de tous les arrondissement dans la bd.
        @return : Une liste des noms d'arrondissements.
        """
        arrondissements = self.db.get_arrondissements()
        return [arr.nom for arr in arrondissements]

    def ajouter_donnees(self, donnees: list[list[str]], nom_table: str):
        """
        Guide l'ajout de ressources vers la bonne table dans la bd.
        @donnees : Une liste de paramètres.
        @nom_table : La table vers laquelle les ressources sont destinées.
        """
        if nom_table == "glissade":
            self.db.ajouter_glissades(donnees)
        elif nom_table == "patinoire":
            self.db.ajouter_patinoires(donnees)
        elif nom_table == "piscine":
            self.db.ajouter_piscines(donnees)

    def get_donnees(self, nom: str) -> list:
        """
        Retourne toutes les ressources contenues par les tables
        'piscine', 'glissade' ou 'patinoire'. Si @nom n'est pas une de ces
        valeurs, retourne None.
        @nom : le nom de la table('piscine', 'glissade' ou 'patinoire')
        @return : Une liste des models.
        """
        return {
            "piscine": self.db.get_piscines(),
            "glissade": self.db.get_glissades(),
            "patinoire": self.db.get_patinoires()
        }.get(nom, None)

    def get_nom_installations(self) -> list:
        """
        Retourne le nom de toutes les installations.
        @return : Une liste contenant le nom de toutes les installations.
        """
        piscines, patinoires, glissades = self.db.get_installations()

        piscines = [piscine.nom for piscine in piscines]
        patinoires = [patinoire.nom for patinoire in patinoires]
        glissades = [glissade.nom for glissade in glissades]
        return piscines + patinoires + glissades

    def get_installation(self, nom_installation: str) -> dict:
        """
        Retourne l'installation correspondant a @nom_installation. Un nom
        d'installation n'est pas unique alors il est possible qu'il y en
        ait plusieurs.

        @nom_installation : Le nom de l'installation recherchée.
        @return Une map contenant les listes possiblement vides des
        installations.
        """
        if nom_installation is None:
            raise TypeError(
                "Vous devez fournir le paramètre 'installation'."
            )
        patinoire = self.db.get_patinoire_avec_nom(nom_installation)
        piscine = self.db.get_piscine_avec_nom(nom_installation)
        glissade = self.db.get_glissade_avec_nom(nom_installation)
        if patinoire is None and piscine is None and glissade is None:
            raise ValueError("Ce nom d'installation n'est pas valide.")
        return {
            "piscines": None if piscine is None else [piscine.as_dict()],
            "patinoires": None if patinoire is None else [patinoire.as_dict()],
            "glissades": None if glissade is None else [glissade.as_dict()]
        }

    def get_installations(self, arrondissement: str) -> dict:
        """
        Retourne toutes les installations d'un arrondissement.
        @arrondissement : Le nom de l'arrondissement pour lequel on recherche
        les installations.
        @return : Une map contenant les installations
        """
        nom_arrondissements = [arrondissement.nom
                               for arrondissement
                               in self.db.get_arrondissements()]
        if arrondissement is None:
            raise TypeError(
                "Vous devez fournir le paramètre 'arrondissement'.")
        elif arrondissement not in nom_arrondissements:
            pres_nom = ', '.join(nom_arrondissements)
            raise ValueError(f"L'arrondissement que vous avec fourni n'est" +
                             " pas valide. Veuillez entrer une des options " +
                             "suivantes : " + pres_nom)
        else:
            piscines, patinoires, glissades = (
                self.db.
                get_installations_avec_arrondissement(arrondissement))
            installations = {
                "piscines": [pisc[1].as_dict() for pisc in piscines],
                "patinoires": [pat[1].as_dict() for pat in patinoires],
                "glissades": [glis[1].as_dict() for glis in glissades]
            }
            return installations
