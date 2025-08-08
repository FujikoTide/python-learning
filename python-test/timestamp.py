from dataclasses import dataclass
from functools import total_ordering


@total_ordering
@dataclass(frozen=True)
class Timestamp:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int

    def __post_init__(self):
        self._basic_validation()

    # nothing too comprehensive but just for the purpose of having something for validation
    def _basic_validation(self):
        if not (
            0 <= self.year
            and 1 <= self.month <= 12
            and 1 <= self.day <= 31
            and 0 <= self.hour < 24
            and 0 <= self.minute < 60
            and 0 <= self.second < 60
        ):
            raise ValueError("Invalid timestamp values")

    def __lt__(self, other):
        if not isinstance(other, Timestamp):
            return NotImplemented

        return (
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
        ) < (other.year, other.month, other.day, other.hour, other.minute, other.second)

    def __eq__(self, other):
        if not isinstance(other, Timestamp):
            return NotImplemented
        return (
            self.year,
            self.month,
            self.day,
            self.hour,
            self.minute,
            self.second,
        ) == (
            other.year,
            other.month,
            other.day,
            other.hour,
            other.minute,
            other.second,
        )


timestamp1 = Timestamp(1999, 11, 30, 12, 34, 23)
timestamp2 = Timestamp(1997, 11, 30, 12, 34, 23)
timestamp3 = Timestamp(2003, 11, 30, 12, 34, 23)


print(timestamp1 > timestamp2)
print(timestamp2 < timestamp3)
print(timestamp3 < timestamp1)
print(timestamp2 > timestamp1)
