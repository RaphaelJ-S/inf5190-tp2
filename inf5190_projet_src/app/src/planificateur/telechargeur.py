
import requests
from pytz import timezone, UTC
from datetime import datetime

from requests.models import Response

from app.src.model.source import Source
from app.src.planificateur.parser.parser import Parser, definir_parser


class Telechargeur:

    def __init__(self, sources: list[Source]):
        self.sources = sources

    def _telecharger(self, url: str, date_modif: datetime, parser: Parser) -> list[list[str]]:
        if parser is None:
            raise ValueError("Le parser utilisé n'est pas valide.")
        raw = requests.get(url)
        if raw.status_code != 200:
            raise TypeError(
                f"telecharger({url}): le téléchargement n'a pas fonctionné. " +
                "Code d'erreur {raw.status_code}")
        if self._a_nouvelles_donnees(raw, date_modif):
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
        donnees = {}
        for source in self.sources:
            url = source.url
            parser = definir_parser(source.parser)
            date_modif = source.date_modif

            print(f"\n\nCommencement du téléchargement de {url}.\n")
            try:
                site_donnees = self._telecharger(url, datetime.fromisoformat(date_modif),
                                                 parser)
                if site_donnees is not None:
                    donnees[source.parser] = site_donnees
                print(f"\n\nTéléchargement de {url} complété.")
            except ValueError as ve:
                print(ve)
            except TypeError as te:
                print(te)
        return donnees
