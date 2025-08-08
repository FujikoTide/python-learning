from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    api_key: str
    log_level: str = "INFO"
    max_retries: int = 3


config = Config("API KEY !!!!")

print(config)

config.log_level = "HELLO"
