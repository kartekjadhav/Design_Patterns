from notifications.notification import (Notification)

class NotificationDecorator(Notification):
    def __init__(self, notification:Notification):
        self._notification = notification
    
    def notify(self, message):
        self._notification.notify(message)