from dataclasses import dataclass


@dataclass
class EmailService:
    def send_message(self, recipient, message):
        return f"An email message to {recipient}\n{message}"


@dataclass
class SMSService:
    def send_message(self, recipient, message):
        return f"An SMS message to {recipient}\n{message}"


@dataclass
class NotificationSystem:
    service: EmailService | SMSService

    def notify(self, recipient, message):
        return self.service.send_message(recipient, message)


email_service = EmailService()
sms_service = SMSService()
send_email = NotificationSystem(email_service)
send_sms = NotificationSystem(sms_service)

print(send_email.notify("Harold", "hello"))
print(send_sms.notify("Harold", "hello again !"))
