from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class Formatter:
    def format_record(self, message, level):
        return self.timestamp_record(f"[{level}] {message}")

    def timestamp_record(self, record):
        current_timestamp = datetime.now()
        return f"[{current_timestamp}] {record}"


class Handler(ABC):
    @abstractmethod
    def emit(self, formatted_record):
        pass


class ConsoleHandler(Handler):
    def emit(self, formatted_record):
        print(formatted_record)


class FileHandler(Handler):
    def emit(self, formatted_record):
        with open("new_logfile.txt", "a") as f:
            print(formatted_record, file=f)


@dataclass
class Logger:
    formatter: Formatter
    handler: Handler

    def info(self, message):
        level = "INFO"
        self.handler.emit(self.formatter.format_record(message, level))

    def error(self, message):
        level = "ERROR"
        self.handler.emit(self.formatter.format_record(message, level))


formatter = Formatter()
console_handler = ConsoleHandler()
file_handler = FileHandler()
console_logger = Logger(formatter, console_handler)
file_logger = Logger(formatter, file_handler)

console_logger.info("hello")
console_logger.error("hello")

file_logger.info("hello")
file_logger.error("hello")
