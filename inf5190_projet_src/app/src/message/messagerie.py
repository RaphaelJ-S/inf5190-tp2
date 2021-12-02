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
            source, twitter, courriel_cible = self.charger_contenu_configuration(
                fich_courriel)
            if source and twitter:
                courriels = self.creer_notifications(
                    courriel_cible, action, models, CourrielBuilder(source))
                tweets = self.creer_notifications(
                    models, action, None, TweetBuilder(twitter)
                )
                self.messages += courriels + tweets

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

    def charger_contenu_configuration(self, nom_fichier: str) -> dict and dict and dict:
        with open(nom_fichier, "r") as file:
            contenu = yaml.safe_load(file)
        courriel = contenu["courriel_envoyant"]
        twitter = contenu["compte_twitter"]
        courriel_cible = contenu["courriel_cible"]
        return courriel, twitter, courriel_cible
