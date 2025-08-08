class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def __repr__(self):
        return f"Temperature(celsius={self.celsius})"

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("Celsius value cannot be below that of absolute zero.")
        self._celsius = value

    @property
    def fahrenheit(self):
        return round((self._celsius * 1.8) + 32, 2)

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self.celsius = (value - 32) / 1.8

    @property
    def kelvin(self):
        return round(self._celsius + 273.15, 2)

    @kelvin.setter
    def kelvin(self, value: float):
        if value < 0:
            raise ValueError("Kelvin cannot be below 0.")
        self.celsius = value - 273.15


temperature = Temperature(45)
# wrong_temperature = Temperature(-400)
print(temperature.fahrenheit)
# print(wrong_temperature.fahrenheit)
