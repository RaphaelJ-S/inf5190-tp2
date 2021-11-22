from requests.models import Response
import xml.etree.ElementTree as ET


class Patinoire_Parser:

    def parse(self, donnees: Response):

        content = donnees.content.decode(donnees.apparent_encoding)
        tree = ET.fromstring(content)
        patinoires = []
        for arrondissement in tree.findall("arrondissement"):
            nom_arr = arrondissement.find("nom_arr").text.strip()
            for patinoire in arrondissement.findall("patinoire"):
                spec_patinoire = []
                conditions = patinoire.findall("condition")
                curr_condition = conditions[-1]
                spec_patinoire.append(curr_condition.find(
                    "date_heure").text.strip())
                spec_patinoire.append(
                    curr_condition.find("deblaye").text.strip())
                spec_patinoire.append(patinoire.find("nom_pat").text.strip())

                spec_patinoire.append(
                    curr_condition.find("arrose").text.strip())
                spec_patinoire.append(
                    curr_condition.find("resurface").text.strip())
                spec_patinoire.append(nom_arr.replace(" - ", "–"))

                patinoires.append(spec_patinoire)
        return patinoires
