from .notification_decorator import NotificationDecorator
from notifications.notification import (Notification)

class FacebookDecorator(NotificationDecorator):
    def __init__(self, notification:Notification):
        super().__init__(notification)
    
    def notify(self, message):
        super().notify(message)
        print(f"Sending Facebook notification -> {message}")