from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, recipients):
        self._recipients = recipients

    @abstractmethod
    def notify(self):
        pass