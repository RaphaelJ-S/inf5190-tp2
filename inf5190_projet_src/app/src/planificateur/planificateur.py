from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.telechargeur import Telechargeur
from app.src.planificateur.maj import MAJ


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
        maj = MAJ(self.db)
