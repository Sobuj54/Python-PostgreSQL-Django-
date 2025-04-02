"""
    🔹 @property Decorator (Getters and Setters):

    The @property decorator converts a method into an attribute.
    This helps in data encapsulation by controlling access to class attributes.
"""

class User:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self.__salary = salary

    """
        Read-Only Property:
        If you don't define a setter, the attribute becomes read-only.
    """
    @property
    def salary(self):  # getter method
        return self.__salary
    
    @salary.setter
    def salary(self, bonus):  # setter method
        self.__salary += bonus
    
naina = User("naina", 21, 25000)
print(naina.salary)  # works
# print(naina.salary()) # doesn't work

naina.salary = 5000  # using the setter method as an attribute
print(naina.salary)  # using the getter method as an attribute
