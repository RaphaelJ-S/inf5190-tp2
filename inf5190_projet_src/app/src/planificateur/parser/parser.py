from typing import Protocol

from requests.models import Response
from app.src.planificateur.parser.glissade_parser import Glissade_Parser
from app.src.planificateur.parser.patinoire_parser import Patinoire_Parser

from app.src.planificateur.parser.piscine_parser import Piscine_Parser


class Parser(Protocol):

    def parse(self, donnees: Response) -> dict[str]:
        pass


def definir_parser(repr: str) -> Parser:
    return {
        "piscine": Piscine_Parser(),
        "patinoire": Patinoire_Parser(),
        "glissade": Glissade_Parser()
    }.get(repr, None)
