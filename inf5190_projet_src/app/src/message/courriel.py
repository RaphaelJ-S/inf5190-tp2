from app.src.message.message import Message


class Courriel(Message):

    def __init__(self, dest: dict[str], info: str):
        self.dest = dest

    def envoyer(self):
        return ""
