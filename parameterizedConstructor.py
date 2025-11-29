class Employee:
    def __init__(self, name, salary):
        self.employeeName = name
        self.salary = salary

if __name__ == "__main__":
    obj = Employee("Tushar", "7 crore")
    print(f"Name: {obj.employeeName}")
    print(f"Salary: Rs.{obj.salary}") 