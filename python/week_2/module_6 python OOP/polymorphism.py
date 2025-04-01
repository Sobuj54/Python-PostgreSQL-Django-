"""
    Polymorphism:

    1. Polymorphism means "many forms". It allows different classes to use the same method name but behave differently based on the object calling it.
"""

# Runtime polymorphism
class Animal:  
    def make_sound(self):
        return "Some sound"

class Dog(Animal):  
    def make_sound(self):  # Overriding parent method
        return "Woof! Woof!"

class Cat(Animal):  
    def make_sound(self):  # Overriding parent method
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Woof! Woof!
print(cat.make_sound())  # Output: Meow!
