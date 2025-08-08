from dataclasses import dataclass


@dataclass
class Notifier:
    def send_notification(self, message):
        return f"here is your message: {message}"

    def get_recipient(self):
        return "dummy recipient"


@dataclass
class EmailNotifier(Notifier):
    def send_notification(self, message):
        return f"here is your email message: {message}"

    def get_recipient(self):
        return "dummy email address"


@dataclass
class SMSNotifier(Notifier):
    def send_notification(self, message):
        return f"here is your SMS message: {message}"

    def get_recipient(self):
        return "dummy phone number"


notifier = Notifier()
email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()

print(notifier)
print(notifier.send_notification("hello"))
print(notifier.get_recipient())
print(email_notifier)
print(email_notifier.send_notification("hello"))
print(email_notifier.get_recipient())
print(sms_notifier)
print(sms_notifier.send_notification("hello"))
print(sms_notifier.get_recipient())
