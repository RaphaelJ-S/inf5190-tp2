

from app.src.db.base_donnees import Base_Donnees


class MAJ:
    def __init__(self, db: Base_Donnees):
        self.db = db

    def _maj_dates(self, nv_donnees: dict):
        self.db.maj_date_sources(list(nv_donnees))

    def _trouver_diff_installations(self, nv_donnees: dict):
        nom_tables = list(nv_donnees)
        print(nv_donnees)
        for nom in nom_tables:
            anc_donnees = self._get_anciennes_donnees(nom)
            diff = self._diff_installation(list(anc_donnees), nv_donnees[nom])

    def _get_anciennes_donnees(self, nom: str) -> list:
        return {
            "piscine": self.db.get_piscines(),
            "glissade": self.db.get_glissades(),
            "patinoire": self.db.get_patinoires()
        }.get(nom, None)

    def _diff_installation(self,
                           anc_donnees: list[list[str]],
                           nv_donnees: list[list[str]]
                           ) -> tuple[list[list[str]]]:
        modif = []
        range_i = len(anc_donnees)
        i = 0
        delta = 0
        while i < range_i:
            curr_donnees = anc_donnees[i]
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

    def _operations_suppression(self, supp: list[list[str]]):
        return print("Suppression : " + supp)

    def _operations_modification(self, modif: list[list[str]]):
        return print("Modification : " + modif)

    def _operations_ajout(self, ajout: list[list[str]]):
        return print("Ajout : " + print(ajout))
