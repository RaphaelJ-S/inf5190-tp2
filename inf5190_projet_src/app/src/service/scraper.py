
import requests
from app.src.service.parser.parser import Parser


class Scraper:
    def __init__(self, sites: dict[str, Parser]):
        self.source = sites

    def telecharger(self, url: str) -> list[list[str]]:
        parser = self.source[url]
        raw = requests.get(url)
        if raw.status_code != 200:
            raise TypeError(
                f"telecharger({url}) : le téléchargement n'a pas fonctionné. Code d'erreur {raw.status_code}")

        return parser.parse(raw)
