import yaml


from app.src.message.builder.courriel_builder import CourrielBuilder
from app.src.message.builder.notification_builder import NotificationBuilder
# from app.src.message.builder.tweet_builder import TweetBuilder
import app.src.util.conversion as conv
from app.src.message.notification.tweet import Tweet
from app.src.message.notification.courriel import Courriel
from app.src.message.notification.notification import Notification


class Messagerie:

    def __init__(self):
        messages = []

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
            self.messages + \
                self.creer_courriels(cibles_courriel, action, models)

            # ajouter le/les tweet ici

    def executer_envois(self):
        for message in self.messages:
            message.envoyer()

    def creer_courriels(self, cibles, action, models) -> list[Notification]:
        messages = []
        for cible in cibles:
            messages.append(self.creer_notification(
                cible, action, models, CourrielBuilder()
            ))
        return messages

    def creer_notification(
            self,
            cible: dict,
            action: str,
            models: list,
            builder: NotificationBuilder) -> Notification:
        builder.ajouter_destinataire(cible)
        builder.ajouter_contenu(action, models)
        return builder.assembler()

    def charger_addresses_courriel(self, nom_fichier: str):
        with open(nom_fichier, "r") as file:
            adresses = yaml.safe_load(file)
        return adresses
