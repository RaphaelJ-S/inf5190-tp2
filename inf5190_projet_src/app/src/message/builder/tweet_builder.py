from app.src.message.builder.notification_builder import NotificationBuilder
from app.src.message.notification.notification import Notification
from app.src.message.notification.tweet import Tweet


class TweetBuilder(NotificationBuilder):

    def __init__(self, compte_twitter):
        self.tweets = []
        self.compte = compte_twitter
    # Cette fonction ne respecte pas les types parce que je n'ai pas fait
    # attention à la conception et qu'il y a des incohérences entres les
    # classes concrètes de NotificationBuilder

    def ajouter_notification(self, dest_info: dict, action: str, donnees: list):
        corps = f"{action} de l'installation {str(dest_info)}"
        self.tweets.append(Tweet(corps, self.compte))

    def assembler(self) -> list[Notification]:
        return self.tweets
