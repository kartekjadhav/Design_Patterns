from notifications.notification import (Notification)
from abc import ABC, abstractmethod

class NotificationDecorator(Notification):
    def __init__(self, notification:Notification):
        self._notification = notification
    
    @abstractmethod
    def notify(self):
        pass