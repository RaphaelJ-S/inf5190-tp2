from apscheduler.schedulers.background import BackgroundScheduler
from app.src.planificateur.telechargeur import Telechargeur
import atexit
import app.src.db.data as database


class Planificateur:

    def __init__(self, frequence: int):
        self.frequence = frequence
        self.sources = database.get_sources()
        self.telechargeur = Telechargeur(self.sources)
        self.travail = BackgroundScheduler(
            timezone="Canada/Eastern", max_instance=1)

    def run(self):
        self.travail.add_job(self.lireSites, 'interval',
                             seconds=self.frequence)
        self.travail.start()
        atexit.register(lambda: self.travail.shutdown())

    def lireSites(self):
        print(
            f"Le travail de téléchargement à interval de {self.frequence} secondes commence.\n\n")
        nv_donnees = self.telechargeur.start()
        print(nv_donnees)
