from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import uuid

from app.src.message.message import Message


class Courriel(Message):

    def __init__(self, sender: dict[str], info_dest: dict[str], action: str, donnees: list):
        self.dest = info_dest
        self.sender = sender
        self.body = self.former_message(action, donnees)

    def envoyer(self, action: str, donnees: list):
        adresse_source = self.sender["email"]
        adresse_dest = self.dest["email"]
        subject = "Mise à jour des installations municipales de récréation."

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = adresse_source
        msg['To'] = adresse_dest

        msg.attach(MIMEText(self.body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(adresse_source, self.sender["mdp"])
        text = msg.as_string()
        server.sendmail(adresse_source, adresse_dest, text)
        server.quit()

    def former_message(self, action: str, donnees: list):
        token = uuid.uuid4().hex
        msg = f"""Des changemetents ont été apportés aux installations d'un arrondissement que vous suivez.
        \n\n {action} des installations suivantes : \n\n"""
        for donnee in donnees:
            msg += str(donnee) + "\n"
        msg += f"""\n\nPour arrêter ces notifications, cliquez sur le lien 
        suivant : http://localhost/desabonne/{token} \n"""
        return msg
