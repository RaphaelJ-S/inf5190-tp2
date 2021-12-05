import yaml


from app.src.message.builder.courriel_builder import CourrielBuilder
from app.src.message.builder.tweet_builder import TweetBuilder
from app.src.message.builder.notification_builder import NotificationBuilder
from app.src.message.notification.notification import Notification


class Messagerie:
    """
    Organise et exécute les envois de notifications(courriel, tweet).
    """

    def __init__(self):
        self.messages = []

    def planifier_envois(self,
                         action: str,
                         models: list,
                         fich_courriel: str = "app/src/fichier/" +
                         "dest_courriel.yaml"):
        """
        Commence le processus de création de notification.
        @action : L'action qui cause la création de notifications.
        @models : Les donnees à envoyer.
        @fich_courriel : Le nom du fichier de configuration contenant les
        adresses.
        """
        if models:
            source, twitter, courriel_cible = (
                self.charger_contenu_configuration(fich_courriel))
            if source and twitter:
                courriels = self.creer_notifications(
                    courriel_cible, action, models, CourrielBuilder(source))
                tweets = self.creer_notifications(
                    models, action, None, TweetBuilder(twitter)
                )
                self.messages += courriels + tweets

    def executer_envois(self):
        """
        Exécute l'envois de toutes les notifications créées.
        """
        for message in self.messages:
            message.envoyer()

    def creer_notifications(
            self, cibles: list, action: str,
            models: list,
            builder: NotificationBuilder) -> list[Notification]:
        """
        Crée les notifications.
        @cibles : Le but des différentes notifications.
        @action : L'action qui cause la création d'une notification.
        @models : Les données destinées aux notification.
        @builder : Le builder à utiliser.
        @return : La liste des notifications créées.
        """
        for cible in cibles:
            builder.ajouter_notification(cible, action, models)
        return builder.assembler()

    def charger_contenu_configuration(
            self,
            nom_fichier: str) -> dict and dict and dict:
        """
        Charge le contenu du fichier @nom_fichier. Ce fichier devrait être
        un fichier .yaml.
        @nom_fichier : le chemin vers le fichier.
        @return : Les informations des différentes partie du fichier.
        en ordre, les informations de l'adresse courriel envoyante ->
        les informations du compte Twitter publiant -> Une liste des
        adresses courriel cibles et leurs informations.
        """
        with open(nom_fichier, "r") as file:
            contenu = yaml.safe_load(file)
        courriel = contenu["courriel_envoyant"]
        twitter = contenu["compte_twitter"]
        courriel_cible = contenu["courriel_cible"]
        return courriel, twitter, courriel_cible
