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
class Student(Family, School, Sports):
    def __init__(self, address, id, level, game):
        Family.__init__(self,address)
        School.__init__(self,id, level)
        Sports.__init__(self,game)

    def show(self):
        print(f"{self.address}, {self.id}, {self.level}, {self.game}")

sobuj = Student("dhaka", 22540,"0","football")
sobuj.show()

        