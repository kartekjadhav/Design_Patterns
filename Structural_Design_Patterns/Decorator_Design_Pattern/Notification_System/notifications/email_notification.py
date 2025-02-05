from .notification import Notification

class EmailNotification(Notification):
    def __init__(self, recipients):
        super().__init__(recipients)
    def notify(self):
        return f"Email notification has been sent {self._recipients}"