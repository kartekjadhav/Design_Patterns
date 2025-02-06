from .notification import Notification

class EmailNotification(Notification):
    def notify(self, message):
        print(f"Sending Email notification -> {message}")