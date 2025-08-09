from config import PRIORITY


class InvalidPriority(ValueError):
    def __init__(self) -> None:
        super().__init__(f"Priority must be one of: {PRIORITY}")
