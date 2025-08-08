from dataclasses import dataclass
from typing import final


class InvalidInputError(Exception):
    def __init__(self, field_name: str, reason: str):
        self.field_name = field_name
        self.reason = reason
        super().__init__(f"Input for {field_name} is invalid because: {reason}")


@final
@dataclass
class UserProfile:
    age: int
    phone_number: int

    def __post_init__(self) -> None:
        self._validate_input()

    def _validate_input(self) -> None:
        self._validate_age(self.age)
        self._validate_phone_number(self.phone_number)

    # simple validation for purposes of demonstration
    def _validate_age(self) -> None:
        """
        Sets the age of the User. Raises an InvalidInputError if the age is of an invalid type.
        """
        if not isinstance(self.age, int):
            raise InvalidInputError("age", "age must be an integer value")
        if self.age < 0:
            raise InvalidInputError("age", "age cannot be negative")

    # simple validation for purposes of demonstration
    def _validate_phone_number(self) -> None:
        """
        Sets the phone number of the user. Raises an InvalidInputError if the phone number if of an invalid type.
        """
        if not isinstance(self.phone_number, int):
            raise InvalidInputError(
                "phone number", "phone number must be an integer value"
            )


try:
    user1 = UserProfile(30, 54756478584)
except InvalidInputError as e:
    print(e)


try:
    user2 = UserProfile("30", 54756478584)
except InvalidInputError as e:
    print(e)


try:
    user3 = UserProfile(30, "54756478584")
except InvalidInputError as e:
    print(e)

try:
    user4 = UserProfile(-5, 3948783759)
except InvalidInputError as e:
    print(e)
