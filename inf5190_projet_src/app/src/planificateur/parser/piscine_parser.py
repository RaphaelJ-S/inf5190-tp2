import csv
from requests.models import Response


class Piscine_Parser:
    """
    application de Parser, parse des données et retourne une liste de
    paramétres.
    """

    def parse(self, donnees: Response) -> list:
        """
        Parse la réponse sous forme de liste de paramètres.
        @données : La réponse d'une requête à une source.
        @return : Une liste de paramètres
        """
        content = donnees.content.decode("utf-8")
        data = list(csv.reader(content.splitlines(), delimiter=','))
        if len(data) >= 1:
            data.pop(0)
        for row in data:
            row[3] = row[3].replace(
                "Pierrefonds-Roxborro", "Pierrefonds–Roxboro").replace(
                    "Ahuntsic-Cartierville", "Ahuntsic–Cartierville"
            )

        return data
