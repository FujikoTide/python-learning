from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class Observer(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass


@dataclass
class Publisher:
    _observers: list[Observer] = field(default_factory=list[Observer])

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


class EmailNotifier(Observer):
    def update(self, message: str) -> None:
        print(f"An email message: {message}")


class SMSNotifier(Observer):
    def update(self, message: str) -> None:
        print(f"An SMS message: {message}")


publisher = Publisher()
email = EmailNotifier()
sms = SMSNotifier()
publisher.attach(email)
publisher.attach(sms)

print("output 2 messages")
publisher.notify("hello")

publisher.detach(sms)

print("output 1 message")
publisher.notify("hello")
