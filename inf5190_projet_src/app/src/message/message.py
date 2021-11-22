from abc import ABC, abstractmethod


class Message(ABC):

    @abstractmethod
    def envoyer(self):
        return
