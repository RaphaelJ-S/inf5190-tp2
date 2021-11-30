from app.src.message.notification.notification import Notification
import tweepy


class Tweet(Notification):

    def __init__(
            self,
            corps: str,
            cle_consom: str = "R5jOEeTafkUzZM14GsAH8NWiR",
            secret_consom: str = "mThUyy1CE4oc6kwKWuqoMR3TZX10DZWbub0nBrnZWcToNegMLQ",
            cle_acces: str = "1465737732538474497-gHPzkhyo8ATWwbbP3zbdD6qb0Qekst",
            secret_acces: str = "Zkce2M8PFtUadhFGef7zQUM1ehkMErWYZn4Kb8QvDpZeX"):
        self.corps = corps
        self.cle_consom = cle_consom
        self.secret_consom = secret_consom
        self.cle_acces = cle_acces
        self.secret_acces = secret_acces

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
