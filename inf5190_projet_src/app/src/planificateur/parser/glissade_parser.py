from requests.models import Response
import xml.etree.ElementTree as ET


class Glissade_Parser:
    """
    application de Parser, parse des données et retourne une liste de
    paramétres.
    """

    def parse(self, donnees: Response) -> list:
        """
        Parse la réponse sous forme de liste de paramètres.
        @données : La réponse d'une requête à une source.
        @return : Une liste de paramètres.
        """
        content = donnees.content.decode(donnees.apparent_encoding)
        tree = ET.fromstring(content)
        glissades = []
        for elem in tree.findall("glissade"):
            glissade = []
            glissade.append(elem.find("ouvert").text)
            glissade.append(elem.find("deblaye").text)
            glissade.append(elem.find("nom").text)

            arrondissement = elem.find("arrondissement")
            glissade.append(arrondissement.find("cle").text)
            glissade.append(arrondissement.find("date_maj").text)
            glissade.append(arrondissement.find(
                "nom_arr").text.replace(" - ", "–"))

            glissades.append(glissade)

        return glissades
