
import requests
from pytz import timezone, UTC
from datetime import datetime

from requests.models import Response

import app.src.db.data as database
from app.src.planificateur.parser.parser import Parser
from app.src.planificateur.parser.glissade_parser import Glissade_Parser
from app.src.planificateur.parser.patinoire_parser import Patinoire_Parser
from app.src.planificateur.parser.piscine_parser import Piscine_Parser


class Telechargeur:

    def _telecharger(self, url: str, date_modif: datetime, parser: Parser) -> list[list[str]]:
        raw = requests.get(url)
        if self._a_nouvelles_donnees(raw, date_modif):
            if raw.status_code != 200:
                raise TypeError(
                    f"telecharger({url}): le téléchargement n'a pas fonctionné. " +
                    "Code d'erreur {raw.status_code}")

            return parser.parse(raw)
        return None

    def _a_nouvelles_donnees(self, raw: Response, date_modif: datetime) -> bool:
        dern_modif = self._convertir_string_vers_date(
            raw.headers["Last-Modified"])
        return date_modif < dern_modif

    def _convertir_string_vers_date(self, date: str) -> datetime:
        est_timezone = timezone("Canada/Eastern")
        str_date = datetime.strptime(
            date, "%a, %d %b %Y %H:%M:%S %Z")
        return str_date.astimezone(UTC).astimezone(est_timezone)

    def start(self):
        sources = database.get_sources()
        for source in sources:
            url = source.url
            parser = source.parser
            date_modif = source.date_modif

            print(f"\n\nCommencement du téléchargement de {url}.\n")
            print(self._telecharger(url, datetime.fromisoformat(date_modif),
                                    self._definir_parser(parser)))

    def _definir_parser(self, repr: str) -> Parser:
        return {
            "piscine": Piscine_Parser(),
            "patinoire": Patinoire_Parser(),
            "glissade": Glissade_Parser()
        }.get(repr, None)
