from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.telechargeur import Telechargeur
from app.src.planificateur.maj import MAJ


class Planificateur:

    def __init__(self, db: Base_Donnees, frequence=None,):
        self.frequence = frequence
        self.db = db
        self.telechargeur = Telechargeur(self.db.get_sources())
        self.travail = BackgroundScheduler(
            timezone="UTC", max_instance=1)

    def run(self):
        self.travail.add_job(
            self.lireSites, 'cron', hour=0
        ) if self.frequence is None else self.travail.add_job(
            self.lireSites, 'interval', seconds=self.frequence
        )

        self.travail.start()
        atexit.register(lambda: self.travail.shutdown())

    def lireSites(self):
        nv_donnees = self.telechargeur.start()
        self.mise_a_jour(nv_donnees)

    def mise_a_jour(self, nv_donnees: dict):
        maj = MAJ(self.db)
        changements = maj.trouver_diff_installations(nv_donnees)
        maj.effectuer_changements(changements)
