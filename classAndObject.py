class Employee:
    def __init__(self):
        # Attributes
        self.employee_name = "" # public
        self._id = ""           # protected
        self.__salary = 0       # private
    
    # Methods to follow (Behaviour)

    def setName(self, name):
        self.employee_name = name

    def setId(self, id):
        self._id = id
    
    def setSalary(self, salary):
        self.__salary = salary
    
    def getName(self):
        return self.employee_name

    def getId(self):
        return self._id


obj = Employee()

obj.setName("Tushar")
obj.setId("abc1234")
obj.setSalary("7 crore")

print(f"Id: {obj.getId()}, Name: {obj.getName()}")