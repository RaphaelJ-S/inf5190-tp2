import yaml

from app.src.message.messagerie import Messagerie
import app.src.util.conversion as conv
from app.src.message.tweet import Tweet
from app.src.message.courriel import Courriel


class Service_Msg:

    def __init__(self, messagerie: Messagerie):

        self.messagerie = messagerie

    def executer_envois(self,
                        action: str,
                        donnees: list[list[str]],
                        nom_table: str,
                        fich_courriel: str = "app/src/fichier/" +
                        "dest_courriel.yaml",
                        compte_twitter: str = ""):
        models = self.convertir_liste_en_model(donnees, nom_table)
        cibles_courriel = self.charger_addresses_courriel(fich_courriel)
        if len(cibles_courriel) >= 1:
            sender = cibles_courriel.pop(0)
            messages = self.creer_courriels(sender, cibles_courriel)
            for message in messages:
                message.envoyer(action, models)
            # ajouter le/les tweet ici

    def convertir_liste_en_model(self,
                                 donnees: list[list[str]],
                                 nom_table: str) -> list:
        donnees_converties = []
        if nom_table == "glissade":
            for donnee in donnees:
                donnees_converties.append(conv.str_vers_glissade(donnee))
        elif nom_table == "patinoire":
            for donnee in donnees:
                donnees_converties.append(conv.str_vers_patinoire(donnee))
        elif nom_table == "piscine":
            for donnee in donnees:
                donnees_converties.append(conv.str_vers_piscine(donnee))
        return donnees_converties

    def creer_courriels(self, sender, cibles):
        messages = []
        messages.append(Courriel(sender, sender))
        for cible in cibles:
            messages.append(Courriel(sender, cible))
        return messages

    def charger_addresses_courriel(self, nom_fichier: str):
        with open(nom_fichier, "r") as file:
            adresses = yaml.safe_load(file)
        return adresses
