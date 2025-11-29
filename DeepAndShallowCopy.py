class Employee:
    def __init__(self, name, salary):
        self.employeeName = name
        self.salary = salary

# Shallow Copy
emp1 = Employee("Tushar", 50000)
emp2 = emp1  # Both reference the same object

emp2.salary = 60000
print(emp1.salary)  # Output: 60000 (original affected)

# Deep Copy
import copy
emp3 = Employee("Tushar", 50000)
emp4 = copy.deepcopy(emp3)  # Independent copy

emp4.salary = 60000
print(emp3.salary)  # Output: 50000 (original unchanged)