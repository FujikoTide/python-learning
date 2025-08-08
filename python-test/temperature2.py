from dataclasses import dataclass


@dataclass
class TemperatureConverter:
    _celsius: float

    @staticmethod
    def _validate_celsius(celsius_value: float):
        if celsius_value < -273.15:
            raise ValueError("Celsius cannot be less than absolute zero: -273.15")

    def __post_init__(self):
        self._validate_celsius(self._celsius)

    @property
    def celsius(self) -> float:
        return round(self._celsius, 2)

    @celsius.setter
    def celsius(self, value: float):
        self._validate_celsius(value)
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        fahrenheit = (self._celsius * 1.8) + 32
        return round(fahrenheit, 2)

    @fahrenheit.setter
    def fahrenheit(self, value):
        celsius = (value - 32) / 1.8
        self.celsius = celsius


temperature = TemperatureConverter(50)
print(temperature)
print(temperature.celsius)
print(temperature.fahrenheit)
# temperature2 = TemperatureConverter(-400)
# print(temperature2)
# print(temperature2.celsius)
