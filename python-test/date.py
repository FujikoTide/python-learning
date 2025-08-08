import calendar
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple


@dataclass
class Date:
    year: int
    month: int
    day: int

    def __post_init__(self):
        self._validate_date()

    # rudimentary checking
    def _validate_date(self):
        if not isinstance(self.year, int):
            raise TypeError("Year must be an int")

        if not (isinstance(self.month, int) and self._validate_value(self.year, 1, 12)):
            raise TypeError("Month must be an int ranging between 1 and 12")

        if isinstance(self.day, int) and self._validate_value(self.year, 1, 31):
            raise TypeError("Day must be an int ranging between 1 and 31")

    def _validate_value(self, value: int, min: int, max: int) -> bool:
        return min <= value <= max


@dataclass
class Calendar:
    @classmethod
    def get_today(cls) -> Date:
        today = datetime.now()
        return Date(today.year, today.month, today.day)

    @staticmethod
    def get_date_info(year: int, month: int, day: int) -> Tuple[int, str, bool]:
        day_of_week: int = calendar.weekday(year, month, day)
        month_name: str = calendar.month_name[month]
        leap_year: bool = calendar.isleap(year)
        return (day_of_week, month_name, leap_year)
