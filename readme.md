# Object Oriented Programming (OOP)
- A programming paradigm, based on the concepts of objects and classes.
- The data is represented as fields (often called **attributes** or **properties**), and the code is represented as **procedure** (often called **methods**).
- **Objects** are instances of classes, which act as blueprints for creating real world entities. 
---

#### Use Cases:
1. High Modularity
2. High Code Reusablity
3. High Security
4. Uses bottom - up approach
5. High Scalability
---

#### `OOP` v/s `POP`
|Feature|OOP|POP|
|:-:|:-:|:-:|
|**Name**|Object Oriented Programming|Procedural Oriented Programming|
|**Focus**|Objects & Data|Functions & Procedures|
|**Data Handling**|Data is hidden & protected (encapsulation)|Data is global & shared|
|**Modularity**|Code is organised into classes & objects|Code is organized into functions|
|**Reusablity**|High|Low|
|**Scalability**|High|Low|
|**Complexity**|High|Low|
|**Appproach**|Bottom - up|Top - down|
|**Security**|High|Low|
|**Example**|`C++`, `Java`|`C`, `Pascal`|
---

#### Classes
- A blueprint or template for creating / calling objects.
- It is the logical representation that defines a set of attributes (data) & methods (function) that the objects created from the class will have.
- Does not occupy any memory on its own.

```python
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
```
---

#### Objects
- An instance of a class.
- When an object is created from a class, memory is allocated for it, and it holds the data as specified by the class.
- It interacts with the other parts of the program, and methods can be called & attributes are accessed that belong to it.

```python
obj = Employee()

obj.setName("Tushar")
obj.setId("abc1234")
obj.setSalary("7 crore")

print(f"Id: {obj.getId()}, Name: {obj.getName()}")
```
Output: 
```text
Id: abc1234, Name: Tushar
```
---


#### Attributes (properties or fields)
- Data or charecterstics of an object.
- Represent state of an object at any given moment.
- Typically defined within a class & can hold different types of information related to the object.
- Also called as `Instance Variables` & are unique.
---

#### Behaviours (methods or functions)
- Actions or operations that an object can perform & are defined in a class.
- Define how the object interacts with its environment or other objects.
- Implemented in methods.
- Represent the functionality of the object.
---

#### Self (keyword)
- Similar to `this` pointer in `C++` or `this` reference in `Java`
- Whenever we call an instance method using an object, address of the object gets passed to the method implicity. The address is collected by the instance method in a variable called `self`
- In place of `self` any other variable name can be used
---

#### Creating a new object
- `__init__()` is invoked automatically whenever, an object is created, whether it is mentioned or not in class description i.e. `constructor`
- It is invoked only `once`
- Object is created in `heap memory`
- `obj = <className>()`
- `__init__()` gurantees initialization & does not return any value
- `Reference` is stored in `stack memory`, because local variable are stored in stack.
---

#### Deletion of an object
- `__del__()` is similar to destructor function
- It gets called automatically when an object goes out of scope. Cleanup activity, if any, should be done in `__del__()`
---

#### Buit - in class methods
1. `vars()`: returns a dictionary of attributes and their values
2. `dir()`: returns a list of attributes
3. `getattr(obj, name, [, default])`: to check if an attribute exists or not 
4. `setattr(obj, name, value)`: to set an attributem if an attribute not exists, then it would be created
5. `delattr(obj, name)`: to delete an attribute
---

#### Built - in class attributes
1. `__dict__`: dictionary containing the class namespace
2. `__name__`: class name
3. `__doc__`: class documentation string or `None` if undefined
4. `__module__`: module name in which the class is defined. This attribute is `__main__` in the interactive mode
5. `__bases__`: a possibly empty tuple containing the base classes, in the order of their occurence in the base class list
---

#### Constructor
- A special method in a class designed to initialize an object when it is created
- It ensures that the object is set up with the required attributes and state before it is used
- It is a method that has the exact same as the class and does not have a return type (not even `void`)
- It is called when an object is created. This justifies why the above code snippets gives the shown output
- If there is no constructor written for the given class, the language by default triggers the default constructor.

```mermaid
flowchart TD;
    Types_of_Contructor-->Parameterized;
    Types_of_Contructor-->Non-Parameterized;
    Types_of_Contructor-->Copy;
    Copy-->Deep_Copy;
    Copy-->Shallow_Copy
```

```python
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
```
Output:
```text
Default values initialized by constructor
Employee Name: Tushar Khanna
Salary: Rs.50000
```

1. **Non - Parameterized Constructor:** A constructor which does not take any arguments as the input

```python
class Employee:
    def __init__(self):
        print("Employee created!")
```

2. **Parameterized Constructor:** It is a type of constructor that accepts arguments to initialize attributes with specific values

```python
class Employee:
    def __init__(self, name, salary):
        self.employeeName = name
        self.salary = salary

if __name__ == "__main__":
    obj = Employee("Tushar", "7 crore")
    print(f"Name: {obj.employeeName}")
    print(f"Salary: Rs.{obj.salary}") 
```

Output:
```text
Name: Tushar
Salary: Rs.7 crore
```

3. **Copy Constructor:** It enables the programmer to create a new object by copying the attribute of an existing object. The purpose of a copy constructor is to create a deep or shallow copy of an object depending on the requirements.
```python
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
```
Output:
```text
60000
50000
```

| Parameter | Shallow Copy | Deep Copy |
|:-:|:-:|:-:|
| **Memory Sharing** | Shares memory locations with the original object | Creates an independent copy with separate memory locations |
| **Performance** | Faster and more efficient, especially for large objects | Slower and may consume more memory |
| **Data Integrity** | May lead to unintended modifications | Ensures data integrity by isolating the copied object |
| **Changes to Copied Object** | Modifications affect the original object and vice versa | Modifications do not affect the original object |
| **Dependencies and References** | Shared references can cause unintended side effects | Handles circular references and complex interdependencies |
---

#### Constructor Chaining
- In python, Constructor Chaining primarily refers to the process of ensuring that when a subclass object is initialized, the constructors of its parent classes are also properly called.
- This ensures that all inherited attributes and behaviors are correctly set up.
- Python utilizes the `super()` function for constructor chaining in inheritance. When you define an `__init__` method (the constructor) in a subclass, it's crucial to explicitly call the `__init__` method of the parent class(es) using `super().__init__()`.
- Python supports multiple inheritance, so `super()` isn’t just “call my parent’s constructor”. It follows something called the **MRO (Method Resolution Order)**—a linear order Python computes to avoid chaos.
- Constructor chaining is particularly useful in scenarios where a class has multiple constructors with different levels of detail for initializing an object. By chaining constructors, duplicating initialization logic can be avoided while maintaining a single point of truth for setting up the object's state.

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # constructor chaining happens here
        self.breed = breed
        print("Dog constructor")

d = Dog("Buddy", "Labrador")
```
Output:
```text
Animal constructor
Dog constructor
```
---

#### Constructor Overloading
- Constructor overloading occurs when a class has more than one constructor, but each constructor has a different parameter list or different parameter type. It allows an object to be initialized in different ways depending on the parameters provided at the time of object creation.
- Python allows only one `__init__` per class. Define it twice and the last one wins—silently.
```python
class Test:
    def __init__(self, a):
        # will be ignored
        self.a = a

    def __init__(self, a, b):
        # will be considered
        self.a = a
        self.b = b
```
- No error. No warning. The first constructor is gone.
- `Python doesn’t support constructor overloading. It replaces it with clarity.`
1. **Default Argument Constructor:** This covers 80% of “overloading” use cases. Simple. Clean. Explicit.
```python
class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
```

2. **Variable arguments (`*args`, `**kwargs`)**: *flexible but dangerous*
Works, but you’re now writing your own argument parser. Use sparingly. Readable code beats clever code every time.
```python
class Point:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0]
            self.y = 0
        elif len(args) == 2:
            self.x, self.y = args
        else:
            raise TypeError("Expected 1 or 2 arguments")
```

3. **Class methods as alternative constructors**: *clean way*
This is the most underrated and powerful pattern.
```python
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
```
- Instead of hiding logic behind multiple constructors, Python nudges you to:
• Make object creation explicit
• Avoid ambiguous argument combinations
• Name intent clearly
- Java-style constructor overloading often hides why an object exists. Python prefers to say it out loud.
---

### OOP's Principles

```mermaid
flowchart TD;
OOP's_Principles-->Encapsulation
OOP's_Principles-->Abstraction
OOP's_Principles-->Inheritance
OOP's_Principles-->Polymorphism
Encapsulation-->Public
Encapsulation-->Private
Encapsulation-->Protected
Abstraction-->Data
Abstraction-->Process
Inheritance-->Single
Inheritance-->Multiple
Inheritance-->Multilevel
Inheritance-->Hierarchical
Inheritance-->Hybrid
Polymorphism-->Run_Time
Polymorphism-->Compile_Time
Run_Time-->Virtual_Functions
Run_Time-->Function_Overriding
Compile_Time-->Function_Overloading
Compile_Time-->Method_Overloading
```

1. **Encapsulation**: 
2. **Abstraction**: 
3. **Inheritance**: 
4. **Polymorphism**: 