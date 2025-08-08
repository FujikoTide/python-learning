from dataclasses import dataclass


@dataclass
class Electronics:
    brand: str
    price: float


@dataclass
class PortableDevice(Electronics):
    battery_life_hours: float


@dataclass
class Smartphone(PortableDevice):
    operating_system: str

    def display_specs(self):
        return f"{self.brand} {self.price} {self.battery_life_hours} {self.operating_system}"


smartphone = Smartphone("nokia", 399, 18, "nokiaOS")
print(smartphone.display_specs())
