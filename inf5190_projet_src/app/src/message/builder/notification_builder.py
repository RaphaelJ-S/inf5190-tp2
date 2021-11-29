from abc import ABC, abstractmethod

from app.src.message.notification.message import Message


class NotificationBuilder(ABC):

    @abstractmethod
    def ajouter_destinataire(self, destinataire: dict):
        pass

    @abstractmethod
    def ajouter_contenu(self, action: str, donnees: list):
        pass

    @abstractmethod
    def assembler(self) -> Message:
        pass
