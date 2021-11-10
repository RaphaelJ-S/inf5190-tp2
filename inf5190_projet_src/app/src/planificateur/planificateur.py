from apscheduler.schedulers.background import BackgroundScheduler
from app.src.planificateur.scraper import Scraper
import atexit


class Planificateur:

    def __init__(self, frequence: int, scraper: Scraper):
        self.frequence = frequence
        self.scraper = scraper
        self.travail = BackgroundScheduler(
            timezone="EST", max_instance=1)

    def run(self):
        self.travail.add_job(self.lireSites, 'interval',
                             seconds=self.frequence)
        self.travail.start()
        atexit.register(lambda: self.travail.shutdown())

    def lireSites(self):
        print(
            f"Le travail de téléchargement à interval de {self.frequence} secondes commence.\n\n")
        self.scraper.start()
