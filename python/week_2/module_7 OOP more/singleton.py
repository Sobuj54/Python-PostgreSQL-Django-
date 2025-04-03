"""
    Singleton Design Pattern in Python 🔥

    The Singleton pattern ensures that only one instance of a class is created throughout the lifetime of a program.
"""

class Singleton:
    __instance = None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception("this is singleton. please call get_instance method")
        
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

first = Singleton()
print(first)
second = Singleton.get_instance()
print(second)