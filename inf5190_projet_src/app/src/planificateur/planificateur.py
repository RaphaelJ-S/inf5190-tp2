from apscheduler.schedulers.background import BackgroundScheduler
import atexit

from app.src.db.base_donnees import Base_Donnees
from app.src.planificateur.telechargeur import Telechargeur
from app.src.planificateur.maj import MAJ
from app.src.service.service import Service


class Planificateur:

    def __init__(self, db: Base_Donnees, frequence=None,):
        self.frequence = frequence
        self.db = db
        sources = self.db.get_sources()
        if not sources:
            db.ajouter_source(
                ["https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-" +
                 "e136158133f2/resource/" +
                 "cbdca706-569e-4b4a-805d-9af73af03b14/" +
                 "download/piscines.csv", "piscine"])
            db.ajouter_source(
                ["https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-" +
                 "a1ce1648a98c/resource/" +
                 "5d1859cc-2060-4def-903f-db24408bacd0/" +
                 "download/l29-patinoire.xml", "patinoire"])
            db.ajouter_source(
                ["http://www2.ville.montreal.qc.ca/services_citoyens/" +
                 "pdf_transfert/L29_GLISSADE.xml", "glissade"])
            sources = self.db.get_sources()

        self.telechargeur = Telechargeur(sources)
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
        self.mise_a_jour(nv_donnees, Service(self.db))

    def mise_a_jour(self, nv_donnees: dict, service: Service):
        maj = MAJ(service)
        changements = maj.trouver_diff_installations(nv_donnees)
        liste_nom_table = maj.effectuer_changements(changements)
        self.db.maj_date_sources(liste_nom_table)
