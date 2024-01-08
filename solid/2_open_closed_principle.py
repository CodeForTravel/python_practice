"""
Software entities (classes, modules, functions, etc.) 
should be open for extension, but closed for modification.
NOTE : This principle use abstract method most of the time(Self realization)
"""

from math import pi
from abc import ABC, abstractmethod


# Normal code
# ==============================================
class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.height = kwargs["height"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]

    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.height
        elif self.shape_type == "circle":
            return pi * self.radius**2


"""
Imagine that you need to add a new shape, maybe a square. How would you do that? Well,
the option here is to add another elif clause to .__init__() and to .calculate_area() 
so that you can address the requirements of a square shape.
"""


# Following SOLID(Open-Closed Principle (OCP))
# ==============================================


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side

    def calculate_area(self):
        return self.side**2


square = Square(5)
print(square.shape_type)
print(square.calculate_area())


# =============================================== Second Example =============================================


# Normal code
# ==============================================
class Employee:
    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary


class Tester(Employee):
    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))


class Developer(Employee):
    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))


class Company:
    def __init__(self, name: str):
        self.name = name

    def work(self, employee):
        if isinstance(employee, Developer):
            employee.develop()
        elif isinstance(employee, Tester):
            employee.test()
        else:
            raise Exception("Unknown employee")


# Following SOLID(Open-Closed Principle (OCP))
# ==============================================
class Employee(ABC):
    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Tester(Employee):
    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))

    def work(self):
        self.test()


class Developer(Employee):
    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))

    def work(self):
        self.develop()


class Company:
    def __init__(self, name: str):
        self.name = name

    def work(self, employee: Employee):
        employee.work()


carbon = Company("Carbon")
developer = Developer("Nusret", "1000000")
tester = Tester("Someone", "1000000")
carbon.work(developer)  # Will print Nusret is developing
carbon.work(tester)  # Will print Someone is testing
