from typing import Protocol

from requests.models import Response


class Parser(Protocol):

    def parse(self, donnees: Response) -> dict[str]:
        pass
