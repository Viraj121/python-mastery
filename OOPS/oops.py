# classes and objects and constructor

class Person:
    def __init__(self,name,age,salary=5000):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

person1=Person("Bob",90)

person1.display()

# encapsulation concept 

class BankAccount:
    def __init__(self,account_number,balance):
        self.acc_no=account_number
        self.__bal=balance

    def deposit(self,amount):
        """Method to deposit money"""
        if amount>0:
            self.__bal+=amount
            print(f"deposited {amount}. New Balance: {self.__bal}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        """Method to withdraw money"""
        if 0 < amount <= self.__bal:
            self.__bal -= amount
            print(f"withdraw {amount}. Remaining Balance: {self.__bal}")
        else:
            print("Invalid withdrawal amount")

    def get_bal(self):
        return self.__bal
    
account=BankAccount("1201290",1000)

account.deposit(8000)
account.withdraw(200)

print("Current Bal:",account.get_bal())

# It differentiates instance attributes from local variables.
# It binds methods to specific objects.
# It allows each object to maintain its own unique data.


# local and instance variable 

class Student:
    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age    # Instance Variable

    def greet(self):
        greeting = f"Hello, my name is {self.name}"  # Local Variable
        print(greeting)  # Local variable used inside the method

# Creating an object
student1 = Student("Alice", 20)

# Accessing instance variables
print(student1.name)  # ✅ Works: Output -> Alice
print(student1.age)   # ✅ Works: Output -> 20

# Calling method
student1.greet()  # ✅ Works: Output -> Hello, my name is Alice

# Trying to access 'greeting' outside the method will cause an error
# print(student1.greeting)  # ❌ AttributeError

# inheritance 

class Animal:
    def __init__(self,name):
        self.name=name

    def make_sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")        

dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.make_sound()
cat.make_sound()

# access modifier

class Person:
    __name = "anonyems"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1=Person()
print(p1.welcome())

