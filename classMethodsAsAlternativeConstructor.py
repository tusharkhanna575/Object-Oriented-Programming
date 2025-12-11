class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_monthly(cls, name, monthly_salary):
        return cls(name, monthly_salary * 12)

    @classmethod
    def from_hourly(cls, name, hourly_rate, hours):
        return cls(name, hourly_rate * hours)

Employee("Alice", 600000)
Employee.from_monthly("Bob", 50000)
Employee.from_hourly("Eve", 500, 1000)
