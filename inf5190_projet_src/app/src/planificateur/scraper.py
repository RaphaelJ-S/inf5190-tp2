
import requests
from app.src.planificateur.parser.glissade_parser import Glissade_Parser
from app.src.planificateur.parser.patinoire_parser import Patinoire_Parser
from app.src.planificateur.parser.piscine_parser import Piscine_Parser

_sitesCible = {
    "https://data.montreal.ca/dataset/4604afb7-a7c4-4626-a3ca-e136158133f2/resource/cbdca706-569e-4b4a-805d-9af73af03b14/download/piscines.csv": Piscine_Parser(),
    "https://data.montreal.ca/dataset/225ac315-49fe-476f-95bd-a1ce1648a98c/resource/5d1859cc-2060-4def-903f-db24408bacd0/download/l29-patinoire.xml": Patinoire_Parser(),
    "http://www2.ville.montreal.qc.ca/services_citoyens/pdf_transfert/L29_GLISSADE.xml": Glissade_Parser()
}


class Scraper:
    def __init__(self):
        self.source = _sitesCible

    def telecharger(self, url: str) -> list[list[str]]:
        parser = self.source[url]
        raw = requests.get(url)
        if raw.status_code != 200:
            raise TypeError(
                f"telecharger({url}) : le téléchargement n'a pas fonctionné. Code d'erreur {raw.status_code}")

        return parser.parse(raw)

    def start(self):
        for url, parser in self.source.items():
            print(f"\n\nCommencement du téléchargement de {url}.\n")
            print(self.telecharger(url))
