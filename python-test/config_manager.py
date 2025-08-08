from dataclasses import dataclass, field
from my_settings import SETTINGS


# basic version of singleton
class ConfigManager:
    _instance = None
    _initialized = False  # Flag to ensure __init__ runs only once

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            # Put your one-time initialization logic here
            self.settings = {"debug_mode": True, "log_file": "app.log"}
            print("ConfigManager initialized for the first time.")
            ConfigManager._initialized = True
        else:
            print("ConfigManager already initialized, skipping.")


@dataclass
class IdiomaticConfigManager:
    _settings: dict = field(default_factory=dict)
    _settings_id: int = 0

    def __post_init__(self):
        if id(SETTINGS) == self._settings_id:
            return
        self._settings = SETTINGS
        self._settings_id = id(SETTINGS)
