from app.src.message.message import Message


class Tweet(Message):

    def __init__(self, compte: str, info: str):
        self.compte = compte

    def envoyer(self):
        return ""
