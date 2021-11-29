from app.src.message.notification.notification import Notification


class Tweet(Notification):

    def __init__(self, compte: str, info: str):
        self.compte = compte

    def envoyer(self, info, action):
        return ""
