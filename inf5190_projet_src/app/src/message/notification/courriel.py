from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from app.src.message.notification.notification import Notification


class Courriel(Notification):

    def __init__(self, adresse: str, corps: str,
                 notifiant: dict[str] = {
                     "email": "raphy.inf5190.labo@gmail.com",
                     "mdp": "Mhs89pz6zrmfhCg"}):
        self.dest = adresse
        self.notifiant = notifiant
        self.corps = corps

    def envoyer(self):
        sujet = "Mise à jour des installations municipales de récréation."

        msg = MIMEMultipart()
        msg['Subject'] = sujet
        msg['From'] = self.notifiant["email"]
        msg['To'] = self.dest

        msg.attach(MIMEText(self.corps, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.notifiant["email"], self.notifiant["mdp"])
        text = msg.as_string()
        server.sendmail(self.notifiant["email"], self.dest, text)
        server.quit()
