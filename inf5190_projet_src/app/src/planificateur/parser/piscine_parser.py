import csv
from requests.models import Response


class Piscine_Parser:

    def parse(self, donnees: Response):
        content = donnees.content.decode("utf-8")
        return list(csv.reader(content.splitlines(), delimiter=','))
