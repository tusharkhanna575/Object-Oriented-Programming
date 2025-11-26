class Employee:
    def __init__(self):
        self.employeeName = "Tushar Khanna"
        self._salary = 50000
    
    def setName(self, name):
        self.employeeName = name
    
    def setSalary(self, val):
        self._salary = val
    
    def getSalary(self):
        return self._salary
    
if __name__ == "__main__":
    obj = Employee()
    print("Default values initialized by constructor")
    print(f"Employee Name: {obj.employeeName}")
    print(f"Salary: Rs.{obj.getSalary()}")