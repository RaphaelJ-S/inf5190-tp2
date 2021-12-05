from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Interface d'envois de notification.
    """

    @abstractmethod
    def envoyer(self):
        return
