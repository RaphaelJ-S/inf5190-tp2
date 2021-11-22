
from app.src.message.message import Message


class Messagerie:

    def __init__(self):
        self.messages = [Message]

    def ajouter_message(self, message: Message):
        self.messages.append(message)

    def executer(self):
        for message in self.messages:
            message.envoyer()
