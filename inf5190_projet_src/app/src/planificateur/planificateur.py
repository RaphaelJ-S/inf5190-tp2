from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.telechargeur import Telechargeur


class Planificateur:

    def __init__(self, frequence: int, db: Base_Donnees):
        self.frequence = frequence
        self.db = db
        self.telechargeur = Telechargeur(self.db.get_sources())
        self.travail = BackgroundScheduler(
            timezone="Canada/Eastern", max_instance=1)

    def run(self):
        self.travail.add_job(self.lireSites, 'interval',
                             seconds=self.frequence)
        self.travail.start()
        atexit.register(lambda: self.travail.shutdown())

    def lireSites(self):
        print(
            f"Le travail de téléchargement à interval de" +
            " {self.frequence} secondes commence.\n\n")
        nv_donnees = self.telechargeur.start()
        self._trouver_diff_installations(nv_donnees)

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
                           ) -> list[list[str]]:
        supp = []
        ajout = []
        modif = []
        range_i = len(anc_donnees)
        i = 0
        while i < range_i:
            delta = self._boucle_interieure(i,
                                            anc_donnees,
                                            nv_donnees,
                                            modif,
                                            supp)
            i -= delta
            range_i -= delta
            i += 1
        if not nv_donnees:
            ajout = nv_donnees

    def _boucle_interieure(self,
                           i: int,
                           anc_donnees: list[list[str]],
                           nv_donnees: list[list[str]],
                           modif: list[list[str]],
                           supp: list[list[str]]) -> int:
        y = 0
        curr_donnees = anc_donnees[i]
        for y in range(len(nv_donnees)):
            if curr_donnees[2] == nv_donnees[y][2]:  # le nom est le même
                # il y a des différences dans les données
                if curr_donnees != nv_donnees[y]:
                    modif.append(nv_donnees[y])
                return self._enlever_elements(i, y, anc_donnees, nv_donnees)

            if y == len(nv_donnees) - 1:
                supp.append(anc_donnees[i])
                return self._enlever_elements(i, y, anc_donnees, nv_donnees)

        return 0

    def _enlever_elements(self, index_i, index_y,
                          anc_donnees: list[list[str]],
                          nv_donnees: list[list[str]]
                          ) -> int:
        anc_donnees.pop(index_i)
        nv_donnees.pop(index_y)
        return 1

    def _operations_suppression(self,
                                anc_donnees: list[list[str]],
                                nv_donnees: list[list[str]]
                                ) -> list[list[str]]:

        return None

    def _operations_modification(self,
                                 anc_donnees: list[list[str]],
                                 nv_donnees: list[list[str]]
                                 ) -> list[list[str]]:
        return None

    def _operations_ajout(self,
                          anc_donnees: list[list[str]],
                          nv_donnees: list[list[str]]
                          ) -> list[list[str]]:

        return None
