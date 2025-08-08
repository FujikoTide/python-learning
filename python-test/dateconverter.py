from dataclasses import dataclass


@dataclass
class Date:
    year: int
    month: int
    day: int

    def __post_init__(self):
        if not (1 <= self.month <= 12):
            raise ValueError("Invalid month")

        if not (1 <= self.day <= 31):
            raise ValueError("Invalid day")

    @classmethod
    def from_string(cls, date_str):
        try:
            year, month, day = map(int, date_str.split("-"))
            return cls(year, month, day)
        except ValueError:
            raise ValueError("Invalid date string.")

    def display_date(self):
        return f"The date is {self.day:02d}/{self.month:02d}/{self.year}"


date1 = Date(2020, 6, 7)
print(date1)
print(date1.display_date())


# Obviously need some work on the various things here
