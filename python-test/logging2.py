from dataclasses import dataclass
from datetime import datetime


@dataclass
class Logger:
    def log(self, message: str):
        print(self.timestamp_message(message))

    def timestamp_message(self, message: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return f"{timestamp}: {message}"


@dataclass
class InfoLogger(Logger):
    def log(self, message):
        super().log(f"[INFO] {message}")


@dataclass
class ErrorLogger(Logger):
    def log(self, message):
        super().log(f"[ERROR] {message}")


log = Logger()
infolog = InfoLogger()
errorlog = ErrorLogger()

log.log("hello")
infolog.log("hello")
errorlog.log("hello")
