import csv
from requests.models import Response


class Piscine_Parser:

    def parse(self, donnees: Response):
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
