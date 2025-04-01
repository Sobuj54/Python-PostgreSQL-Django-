"""
    Multiple Inheritance

    1. A class that inherits from more than one class

"""

class Family:
    def __init__(self, address):
        self.address = address

class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level

class Sports:
    def __init__(self,game):
        self.game = game

# multiple inheritance
class Student:
    def __init__(self, address, id, level, game):
        Family.__init__(self,address)
        School.__init__(self,id, level)
        Sports.__init__(self,game)
        