from abc import ABC, abstractmethod


class Message(ABC):

    @abstractmethod
    def envoyer(self, action, donnees):
        return

    @abstractmethod
    def former_message(actions: str, donnees: list):
        return
