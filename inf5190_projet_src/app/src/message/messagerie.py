import yaml


from app.src.message.builder.courriel_builder import CourrielBuilder
from app.src.message.builder.tweet_builder import TweetBuilder
from app.src.message.builder.notification_builder import NotificationBuilder
from app.src.message.notification.notification import Notification


class Messagerie:

    def __init__(self):
        self.messages = []

    def planifier_envois(self,
                         action: str,
                         models: list,
                         fich_courriel: str = "app/src/fichier/" +
                         "dest_courriel.yaml"):
        if models:
            cibles_courriel = self.charger_addresses_courriel(fich_courriel)
            if len(cibles_courriel) >= 1:
                courriels = self.creer_notifications(
                    cibles_courriel, action, models, CourrielBuilder())
                tweets = self.creer_notifications(
                    models, action, None, TweetBuilder()
                )
                self.messages += courriels + tweets

            # ajouter le/les tweet ici

    def executer_envois(self):
        for message in self.messages:
            message.envoyer()

    def creer_notifications(
            self, cibles: dict, action: str,
            models: list,
            builder: NotificationBuilder) -> list[Notification]:
        for cible in cibles:
            builder.ajouter_notification(cible, action, models)
        return builder.assembler()

    def charger_addresses_courriel(self, nom_fichier: str):
        with open(nom_fichier, "r") as file:
            adresses = yaml.safe_load(file)
        return adresses
