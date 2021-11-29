from abc import ABC, abstractmethod

from app.src.message.notification.notification import Notification


class NotificationBuilder(ABC):

    @abstractmethod
    def ajouter_notification(self, dest_info: dict,
                             action: str, donnees: list):
        pass

    @abstractmethod
    def assembler(self) -> list[Notification]:
        pass
