# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Ali", 90)
s1.display()

# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("Total objects:", cls.count)

c1 = Counter()
c2 = Counter()
Counter.show_count()

# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "Car is starting...")

car1 = Car("Toyota")
print(car1.brand)
car1.start()

# 4. Class Variables and Class Methods
class Bank:
    bank_name = "Old Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1 = Bank()
b2 = Bank()
print(b1.bank_name)
Bank.change_bank_name("New Bank")
print(b2.bank_name)

# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 4))

# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger started")

    def __del__(self):
        print("Logger ended")

log = Logger()
del log

# 7. Access Modifiers: Public, Protected, Private
class Employee:
    def __init__(self):
        self.name = "Ahmed"         # Public
        self._salary = 50000        # Protected
        self.__ssn = "123-45-6789"  # Private

emp = Employee()
print(emp.name)
print(emp._salary)
# print(emp.__ssn)  # Will give error
print(emp._Employee__ssn)  # Accessing private (not recommended)

# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t1 = Teacher("Sara", "Math")
print(t1.name, "-", t1.subject)

# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

r = Rectangle(4, 5)
print("Area:", r.area())

# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name, "is barking!")

d = Dog("Rex", "German Shepherd")
d.bark()

# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print("Books:", Book.total_books)

# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))

# 13. Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

e = Engine()
c = Car(e)
c.start_engine()

# 14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, emp):
        self.emp = emp

emp1 = Employee("Maha")
dept = Department(emp1)
print(dept.emp.name)

# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()  # MRO: B > C > A

# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.greet())

# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

prod = Product(100)
print(prod.price)
prod.price = 150
print(prod.price)
del prod.price

# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

m = Multiplier(3)
print(callable(m))
print(m(10))

# 20. Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Valid age")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)

# 21. Custom Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)
