
from app.src.service.scraper import Scraper
import app.src.base_donnees.data as database
from app.src.service.parser.piscine_parser import Piscine_Parser
from app.src.service.parser.patinoire_parser import Patinoire_Parser
from app.src.service.parser.glissade_parser import Glissade_Parser


sitesCible = {
    "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv": Piscine_Parser(),
    "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml": Patinoire_Parser(),
    "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml": Glissade_Parser()
}


def lireSite():
    scraper = Scraper(sitesCible)
    keys = list(sitesCible)
    tele = scraper.telecharger(keys[2])
    print(tele)


def ajouter_piscine():
    toutes_piscines = list(cr)
    toutes_piscines[1][7] = toutes_piscines[1][7].replace(",", ".")
    print(toutes_piscines[1][7])
    database.ajouter_piscine(toutes_piscines[1])
