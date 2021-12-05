import uuid

from app.src.message.builder.notification_builder import NotificationBuilder
from app.src.message.notification.courriel import Courriel
from app.src.message.notification.notification import Notification


class CourrielBuilder(NotificationBuilder):
    """
    Implémentation de NotificationBuilder.
    Utilisé pour construire une liste de courriels.
    """

    def __init__(self, adresse_source):
        self.courriels = []
        self.source = adresse_source

    def ajouter_notification(self, dest_info: dict,
                             action: str, donnees: list):
        """
        Ajoute un courriel à la liste finale.
        @dest_info : les informations du destinataire
        (nom, adresse, arrondissements).
        @action : L'action qui cause l'envois d'une notification
        ('ajout', 'suppression', 'modification')
        @donnees : Les informations à envoyer.
        """
        try:
            adresse = dest_info["email"]
            nom = dest_info["nom"]
            liste_arr = dest_info["liste_arr"]
            corps = self.former_corps(action, donnees, nom, liste_arr)
            self.courriels.append(Courriel(adresse, corps, self.source))

        except TypeError as ve:
            print(f"ajouter_notification : " +
                  "Erreur dans la création d'une notification. {adresse}\n" +
                  "{ve}")

    def former_corps(self, action: str, donnees: list,
                     nom: str, liste_arr: list[str]) -> str:
        """
        Retourne le 'corps' du courriel.
        @action : L'action qui cause l'envois d'une notification
        ('ajout','suppression', 'modification')
        @donnees : Les informations à envoyer.
        @nom : Le nom du destinataire.
        @liste_arr : Les arrondissements qui intéressent le destinataire.
        @return : Le message à envoyer au destinataire.
        """
        token = uuid.uuid4().hex
        msg = f"""Bonjour {nom}.\n
        Des changements ont été apportés aux installations d'un
        arrondissement que vous suivez.
        \n\n {action} des installations suivantes : \n\n"""
        for donnee in self.filtrer_arrondissement(donnees, liste_arr):
            msg += str(donnee) + "\n"
        msg += f"""\n\nPour arrêter ces notifications, cliquez sur le lien 
        suivant : http://localhost/desabonne/{token} \n"""
        return msg

    def filtrer_arrondissement(self, donnees: list,
                               liste_arr: list[str]) -> list:
        """
        Filtre les données selon les arrondissements
        qui intéressent le destinataire.
        @donnees : Les donnees à envoyer.
        @liste_arr : Les arrondissements qui intéressent le destinataire.
        @return : Les données filtrées.
        """
        return donnees

    def assembler(self) -> list[Notification]:
        """
        Retourne la liste des courriels prêts à être envoyés.
        """
        return self.courriels
