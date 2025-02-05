import notifications
import notification_decorators
from inspect import isclass, isabstract, getmembers

if __name__ == "__main__":
    NM = getmembers(notifications, lambda n: isclass(n) and not isabstract(n) and issubclass(n, notifications.Notification))
    NMD = getmembers(notification_decorators, lambda n: isclass(n) and not isabstract(n) and issubclass(n, notification_decorators.NotificationDecorator))

    notification_members = {key:value for key, value in NM}
    notification_decorator_members = {key:value for key, value in NMD}

    noti = notification_members["EmailNotification"](["Om", "Kartek", "Sid"])
    fb_noti = notification_decorator_members["FacebookDecorator"](noti)
    print(fb_noti.notify())
    slack_noti = notification_decorator_members["SlackDecorator"](noti)
    print(slack_noti.notify())