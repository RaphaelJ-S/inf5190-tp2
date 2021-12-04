from requests.models import Response
import xml.etree.ElementTree as ET


class Patinoire_Parser:
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
                spec_patinoire.append(nom_arr.replace(
                    " - ", "–").replace("Villeray-Saint-Michel–Parc-Extension",
                                        "Villeray–Saint-Michel–Parc-Extension")
                )
                patinoires.append(spec_patinoire)
        return patinoires
