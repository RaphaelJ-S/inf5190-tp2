from requests.models import Response
import xml.etree.ElementTree as ET


class Glissade_Parser:

    def parse(self, donnees: Response):
        content = donnees.content
        tree = ET.fromstring(content)
        glissades = []
        for elem in tree.findall("glissade"):
            glissade = []
            glissade.append(elem.find("nom").text)
            glissade.append(elem.find("ouvert").text)
            glissade.append(elem.find("deblaye").text)

            arrondissement = elem.find("arrondissement")
            glissade.append(arrondissement.find("nom_arr").text)
            glissade.append(arrondissement.find("cle").text)
            glissade.append(arrondissement.find("date_maj").text)
            glissades.append(glissade)

        return glissades
