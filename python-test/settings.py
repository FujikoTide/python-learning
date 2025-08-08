from dataclasses import dataclass


@dataclass
class UserSettings:
    theme: str
    font_size: int
    language: str

    @classmethod
    def default_settings(cls):
        return cls("dark", 16, "en")


default_settings = UserSettings.default_settings()
custom_settings = UserSettings("light", 12, "de")
