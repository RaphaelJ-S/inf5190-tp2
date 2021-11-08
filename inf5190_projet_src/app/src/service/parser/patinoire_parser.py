from requests.models import Response
import xml.etree.ElementTree as ET


class Patinoire_Parser:

    def parse(self, donnees: Response):
        content = donnees.content
        tree = ET.fromstring(content)
        arrondissements = dict()
        for arrondissement in tree.findall("arrondissement"):
            patinoires = []
            nom = ""
            for nom_pat in arrondissement.findall("nom_arr"):
                nom = nom_pat.text.strip()
            for patinoire in arrondissement.findall("patinoire"):

                for condition in patinoire.iterfind("condition"):
                    conditions = []
                    conditions.append(condition.find(
                        "date_heure").text.strip())
                    conditions.append(condition.find("deblaye").text.strip())
                    conditions.append(condition.find("arrose").text.strip())
                    conditions.append(condition.find("resurface").text.strip())
                    patinoires.append(conditions)
            arrondissements[nom] = patinoires
        return arrondissements
