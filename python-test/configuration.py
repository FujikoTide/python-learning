from dataclasses import dataclass


@dataclass
class Configuration:
    _database_url: str
    _api_key: str

    @staticmethod
    def validate_input(value: str, field_name: str):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value:
            raise ValueError(f"{field_name} is required")

    def __post_init__(self):
        self.validate_input(self._api_key, "API Key")
        self.validate_input(self._database_url, "Database URL")

    @property
    def database_url(self) -> str:
        return self._database_url

    @property
    def api_key(self) -> str:
        return self._api_key

    @database_url.setter
    def database_url(self, value: str):
        self.validate_input(value, "Database URL")
        self._database_url = value

    @api_key.setter
    def api_key(self, value: str):
        self.validate_input(value, "API Key")
        self._api_key = value


try:
    config = Configuration("www.testing.com", "hahahahaha")
    print(config)
    print(config.api_key)
    print(config.database_url)
    config.api_key = "huhuhuhuhu"
    config.database_url = "www.somethingelse.com"
    print(config)
    print(config.api_key)
    print(config.database_url)
    config.database_url = ""
    config.api_key = 43535545
except (ValueError, TypeError) as e:
    print(f"Some errors occurred. {e}")
