import uuid

from app.src.message.builder.notification_builder import NotificationBuilder
from app.src.message.notification.courriel import Courriel
from app.src.message.notification.notification import Notification


class CourrielBuilder(NotificationBuilder):

    def __init__(self, adresse_source):
        self.courriels = []
        self.source = adresse_source

    def ajouter_notification(self, dest_info: dict,
                             action: str, donnees: list):
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
        return donnees

    def assembler(self) -> list[Notification]:
        return self.courriels
