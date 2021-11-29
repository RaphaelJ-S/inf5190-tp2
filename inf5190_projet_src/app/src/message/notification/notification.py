from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def envoyer(self):
        return
