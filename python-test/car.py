class Car:
  def __init__(self, make: str, model: str):
    self.make = make
    self.model = model
    self._speed: int = 0

  def __repr__(self):
    return (f"Car(make={self.make}, model={self.model}, speed={self._speed})")  

  def accelerate(self, amount: int):
    self._speed += amount

  def brake(self, amount: int):
    if amount > self._speed:
      amount = self._speed
    self._speed -= amount

  @property
  def speed(self) -> int:
    return self._speed
  
  
car = Car("Nissan", "Sunny")
print(car)
print(car.speed)
car.accelerate(20)
print(car.speed)
car.brake(10)
print(car.speed)
car.accelerate(30)
print(car.speed)
car.brake(15)
print(car.speed)
car.accelerate(20)
print(car.speed)
car.brake(5)
print(car.speed)
print(car)