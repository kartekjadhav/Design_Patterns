from .notification_decorator import NotificationDecorator
from notifications.notification import (Notification)

class SlackDecorator(NotificationDecorator):
    def __init__(self, notification:Notification):
        super().__init__(notification)
    
    def notify(self):
        return self._notification.notify() + " + Slack Notification"