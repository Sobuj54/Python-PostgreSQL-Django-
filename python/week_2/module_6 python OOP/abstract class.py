"""
    Abstract class

    1. An abstract class is a class that cannot be instantiated directly. It serves  as a blueprint for other classes and often contains abstract methods that must  be implemented by child classes.
    
    2. Python provides the ABC (Abstract Base Class) module from abc to define abstract classes.
"""

from abc import ABC, abstractmethod

class Animal(ABC):   # Abstract class
    @abstractmethod
    def eat(self):   # Abstract method (no implementation)
        pass

    @abstractmethod
    def move(self):
        pass

    """
       Features of abstract class:

       1. Cannot create an object of an abstract class
       2. Forces child classes to implement abstract methods. 
       3. Contains abstract methods (methods without implementation).
    """

class Monkey(Animal):
    def __init__(self,name):
        self.category = "Monkey"
        self.name = name
        super().__init__()

    def eat(self):
        print(f"{self.name} is eating banana")

    def move(self):
        pass

red_tail = Monkey("red tail")
print(red_tail.name)
red_tail.eat()