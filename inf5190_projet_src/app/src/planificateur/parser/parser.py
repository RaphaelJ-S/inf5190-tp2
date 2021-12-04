from typing import Protocol
from requests.models import Response

from app.src.planificateur.parser.glissade_parser import Glissade_Parser
from app.src.planificateur.parser.patinoire_parser import Patinoire_Parser
from app.src.planificateur.parser.piscine_parser import Piscine_Parser


class Parser(Protocol):
    """
    Interface pour les classes faisant du parsing.
    """

    def parse(self, donnees: Response) -> list:
        pass


def definir_parser(repr: str) -> Parser:
    """
    Retourne une instance du parser correspondant à @repr.
    @repr : Une chaîne('piscine', 'patinoire' ou 'glissade').
    @return : Une instance concrète de Parser.
    """
    return {
        "piscine": Piscine_Parser(),
        "patinoire": Patinoire_Parser(),
        "glissade": Glissade_Parser()
    }.get(repr, None)
