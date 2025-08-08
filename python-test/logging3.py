from dataclasses import dataclass
from datetime import datetime


@dataclass
class AbstractLogger:
    def log(self, level, message):
        return self.timestamp(f"[{level}] {message}")

    def timestamp(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        return f"[{timestamp}] {message}"


@dataclass
class ConsoleLogger(AbstractLogger):
    def log(self, level, message):
        print(super().log(level, message))


@dataclass
class FileLogger(AbstractLogger):
    def log(self, level, message):
        with open("logfile.txt", "a") as f:
            f.write(f"{super().log(level, message)}\n")


console_logger = ConsoleLogger()
file_logger = FileLogger()

console_logger.log("INFO", "test1")
console_logger.log("WARNING", "test2")
console_logger.log("ERROR", "test3")

file_logger.log("INFO", "test1")
file_logger.log("WARNING", "test2")
file_logger.log("ERROR", "test3")
