import yaml

from app.src.message.messagerie import Messagerie
import app.src.util.conversion as conv
from app.src.message.tweet import Tweet
from app.src.message.courriel import Courriel


class Service_Msg:

    def __init__(self, messagerie: Messagerie):

        self.messagerie = messagerie

    def planifier_envois(self,
                         action: str,
                         donnees: list[list[str]],
                         nom_table: str,
                         fich_courriel: str = "app/src/fichier/" +
                         "dest_courriel.yaml",
                         compte_twitter: str = ""):
        models = conv.convertir_liste_en_model(donnees, nom_table)
        cibles_courriel = self.charger_addresses_courriel(fich_courriel)
        if len(cibles_courriel) >= 1:
            sender = cibles_courriel.pop(0)
            self.ajouter_courriels(
                self.creer_courriels(sender, cibles_courriel, action, models))

            # ajouter le/les tweet ici

    def executer_envois(self):
        self.messagerie.executer()

    def creer_courriels(self, sender, cibles, action, models) -> list[Courriel]:
        messages = []
        messages.append(Courriel(sender, sender, action, models))
        for cible in cibles:
            messages.append(Courriel(sender, cible, action, models))
        return messages

    def ajouter_courriels(self, list_courriel: list[Courriel]):
        for courriel in list_courriel:
            self.messagerie.ajouter_message(courriel)

    def charger_addresses_courriel(self, nom_fichier: str):
        with open(nom_fichier, "r") as file:
            adresses = yaml.safe_load(file)
        return adresses
