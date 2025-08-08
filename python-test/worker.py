from dataclasses import dataclass, field


@dataclass
class Worker:
    name: str
    _salary: float = field(init=False)

    def __post_init__(self):
        self._salary = 0

    def work(self):
        return "working !"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, amount):
        self._salary = amount


@dataclass
class HourlyWorker(Worker):
    hours_worked: float
    hourly_rate: float

    def work(self):
        return "working for an hour !!!"

    @property
    def salary(self):
        return self.hours_worked * self.hourly_rate


@dataclass
class SalariedWorker(Worker):
    annual_salary: float

    def work(self):
        return "working for a whole year !!!!!!"

    @property
    def salary(self):
        return self.annual_salary


worker = Worker("Harold")
hourly_worker = HourlyWorker("George", 5, 56)
salaried_worker = SalariedWorker("Sue", 456743)

print(worker)
print(worker.work())
print(worker.name)
print(worker.salary)
print(hourly_worker)
print(hourly_worker.work())
print(hourly_worker.name)
print(hourly_worker.hourly_rate)
print(hourly_worker.hours_worked)
print(hourly_worker.salary)
print(salaried_worker)
print(salaried_worker.work())
print(salaried_worker.name)
print(salaried_worker.annual_salary)
print(salaried_worker.salary)
