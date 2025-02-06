import notifications
import notification_decorators
from inspect import isclass, isabstract, getmembers

if __name__ == "__main__":
    NM = getmembers(notifications, lambda n: isclass(n) and not isabstract(n) and issubclass(n, notifications.Notification))
    NMD = getmembers(notification_decorators, lambda n: isclass(n) and not isabstract(n) and issubclass(n, notification_decorators.NotificationDecorator))

    notification_members = {key:value for key, value in NM}
    decorator_members = {key:value for key, value in NMD}

    print(f"Base Notifiers -> {notification_members}")
    val = input("Enter the base notifier you want from above: ").strip()
    notifier = notification_members[val]()

    notifier = decorator_members["FacebookDecorator"](notifier)
    notifier = decorator_members["SlackDecorator"](notifier)
    notifier = decorator_members["SmsDecorator"](notifier)

    notifier.notify("Your house is on fire")


    #SMS(Slack(Facebook(Email())))