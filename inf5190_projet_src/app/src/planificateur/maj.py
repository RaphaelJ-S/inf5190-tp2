

from app.src.db.base_donnees import Base_Donnees


class MAJ:
    def __init__(self, db: Base_Donnees):
        self.db = db

    def _maj_dates(self, nv_donnees: dict):
        self.db.maj_date_sources(list(nv_donnees))

    def trouver_diff_installations(self, nv_donnees: dict):
        nom_tables = list(nv_donnees)
        changements = {}
        for nom in nom_tables:
            anc_donnees = self._get_anciennes_donnees(nom)
            diff = self._diff_installation(
                anc_donnees, nv_donnees[nom])
            changements[nom] = diff
        return changements

    def _get_anciennes_donnees(self, nom: str) -> list[list[str]]:
        return {
            "piscine": self.db.get_piscines(),
            "glissade": self.db.get_glissades(),
            "patinoire": self.db.get_patinoires()
        }.get(nom, None)

    def _diff_installation(self,
                           anc_donnees: list,
                           nv_donnees: list[list[str]]
                           ) -> tuple[list[list[str]]]:
        modif = []
        range_i = len(anc_donnees)
        i = 0
        delta = 0
        while i < range_i:
            curr_donnees = anc_donnees[i].as_partial_list()
            for y in range(len(nv_donnees)):
                if curr_donnees[2] == nv_donnees[y][2]:  # le nom est le même
                    # S'il y a des différences dans les données
                    if curr_donnees != nv_donnees[y]:
                        modif.append(nv_donnees[y])
                    delta = self._enlever_elements(
                        i, y, anc_donnees, nv_donnees)
                    break
            i -= delta - 1
            range_i -= delta
            delta = 0
        return (nv_donnees, anc_donnees, modif)

    def _enlever_elements(self, index_i, index_y,
                          anc_donnees: list[list[str]],
                          nv_donnees: list[list[str]]
                          ) -> int:
        anc_donnees.pop(index_i)
        nv_donnees.pop(index_y)
        return 1

    def effectuer_changements(self, a_effectuer: dict[str, tuple[list[list[str]]]]):
        liste_nom_table = list(a_effectuer)
        for nom in liste_nom_table:
            self.operations_ajout(a_effectuer[nom][0], nom)
            # Ces fonctionnalités ne font pas partie du TP mais elle sont
            # gardées pour développement futur
            self.operations_suppression(a_effectuer[nom][1], nom)
            self.operations_modification(a_effectuer[nom][2], nom)

        self.db.maj_date_sources(liste_nom_table)

    def operations_suppression(self, supp: list[list[str]], table: str):
        return  # print("Suppression dans " + table + " : " + str(supp))

    def operations_modification(self, modif: list[list[str]], table: str):
        return  # print("Modification dans " + table + " : " + str(modif))

    def operations_ajout(self, ajout: list[list[str]], table: str):
        if table == "glissade":
            self.db.ajouter_glissades(ajout)
        elif table == "patinoire":
            self.db.ajouter_patinoires(ajout)
        elif table == "piscine":
            self.db.ajouter_piscines(ajout)
