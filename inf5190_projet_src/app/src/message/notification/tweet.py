from app.src.message.notification.notification import Notification
import tweepy


class Tweet(Notification):

    def __init__(
            self,
            corps: str,
            info_compte: dict):
        self.corps = corps
        self.cle_consom = info_compte["cle_consomateur"]
        self.secret_consom = info_compte["secret_consomateur"]
        self.cle_acces = info_compte["cle_acces"]
        self.secret_acces = info_compte["secret_acces"]

    def envoyer(self):
        try:
            authentification = tweepy.OAuthHandler(
                self.cle_consom, self.secret_consom)
            authentification.set_access_token(
                self.cle_acces, self.secret_acces)
            api = tweepy.API(authentification)
            api.update_status(self.corps)
        except tweepy.errors.Forbidden:
            print(f"Ce tweet n'a pas pu être publié : {self.corps}")
