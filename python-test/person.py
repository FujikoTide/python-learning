from dataclasses import dataclass, field
from datetime import date


@dataclass
class Person:
    name: str
    birth_year: int
    _age: int = field(init=False)

    def __post_init__(self):
        self._age = date.today().year - self.birth_year

    @property
    def age(self):
        return self._age


bob = Person("bob", 1980)
print(bob.name)
print(bob.age)
