
import requests
from datetime import datetime
from requests.models import Response

from app.src.util.dates import convertir_str_vers_date_ET_avec_offset
from app.src.model.source import Source
from app.src.planificateur.parser.parser import Parser, definir_parser


class Telechargeur:
    """
    S'occupe du téléchargement et du parsing des différentes Sources données.
    """

    def __init__(self, sources: list[Source]):
        self.sources = sources

    def _telecharger(self, url: str,
                     date_modif: datetime,
                     parser: Parser) -> list[list[str]]:
        """
        Télécharge @url et le parse si il y a de nouvelles données.
        @url : l'url de la source à télécharger.
        @date_modif : La date de la dernière fois que cette source a été
        téléchargée.
        @parser : Le parser a utiliser pour cette source.
        @return : Les données de la source parsées ou None s'il n'y a pas de
        changements à apporter.
        """
        if parser is None:
            raise ValueError("Le parser utilisé n'est pas valide.")
        raw = requests.get(url)
        if raw.status_code != 200:
            raise TypeError(
                f"telecharger({url}): le téléchargement n'a pas fonctionné." +
                " Code d'erreur {raw.status_code}")
        if self._a_nouvelles_donnees(raw, date_modif):
            return parser.parse(raw)
        return None

    def _a_nouvelles_donnees(self,
                             raw: Response,
                             date_modif: datetime) -> bool:
        dern_modif = convertir_str_vers_date_ET_avec_offset(
            raw.headers["Last-Modified"])
        return date_modif < dern_modif

    def start(self) -> dict:
        """
        Commence le processus de téléchargement de toutes les sources données.
        @return : Une map des données téléchargés.
        """
        donnees = {}
        for source in self.sources:
            url = source.url
            parser = definir_parser(source.parser)
            date_modif = source.date_modif

            print(f"\n\nCommencement du téléchargement de {url}.\n")
            try:
                site_donnees = self._telecharger(
                    url, datetime.fromisoformat(date_modif), parser)
                if site_donnees is not None:
                    donnees[source.parser] = site_donnees
                print(f"\n\nTéléchargement de {url} complété.")
            except ValueError as ve:
                print(ve)
            except TypeError as te:
                print(te)
        return donnees
