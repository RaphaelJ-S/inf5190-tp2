

from app.src.message.notification.courriel import Courriel
import uuid


class CourrielBuilder:

    def __init__(self):
        self.dest_nom = "Anonyme"
        self.dest_adresse = "none_inf5190@gmail.com"
        self.list_arr = []
        self.corps = ""

    def ajouter_destinataire(self, destinataire: dict):
        self.dest_nom = destinataire["nom"]
        self.dest_adresse = destinataire["email"]
        self.list_arr = destinataire["liste_arr"]

    def ajouter_message(self, action: str, donnees: list):
        token = uuid.uuid4().hex
        msg = f"""Bonjour {self.dest_nom}.\n
        Des changements ont été apportés aux installations d'un
        arrondissement que vous suivez.
        \n\n {action} des installations suivantes : \n\n"""
        for donnee in donnees:
            msg += str(donnee) + "\n"
        msg += f"""\n\nPour arrêter ces notifications, cliquez sur le lien 
        suivant : http://localhost/desabonne/{token} \n"""
        self.corps = msg

    def assembler(self) -> Courriel:
        return Courriel(self.dest_adresse, self.corps)
