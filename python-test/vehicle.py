from dataclasses import dataclass


@dataclass
class Vehicle:
    brand: str
    year: int


@dataclass
class Car(Vehicle):
    model: str

    def display_info(self):
        return f"{self.brand} {self.model} {self.year}"


car = Car("Honda", 1990, "NSX")
print(car.display_info())
