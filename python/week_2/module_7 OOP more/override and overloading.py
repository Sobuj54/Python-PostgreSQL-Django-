class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def eat(self):
        print("vat khao")
    
    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, profession, country):
        self.country = country
        super().__init__(name, age, profession)

    # function overriding
    def eat(self):  #overriding parent eat function
        print("healthy khao")

    def exercise(self):
        print("beyam koro")

    # + sign overloading
    def __add__(self, other):
        return self.age + other.age
    
    # * sign overloading
    def __mul__(self, other):
        return self.age * other.age
    
    # - sign overloading
    def __sub__(self, other):
        return self.age - other.age
    
    # > sign overloading
    def __gt__(self, other):
        return self.age > other.age
    
sakib = Cricketer("sakib al hasan",35,"cricketer", "BD")
sakib.eat()
sakib.exercise()
mushi = Cricketer("mushi", 32, "cricketer", "BD")

# operator overloading
# + sign overloading
print(10+20)  # normal
print("sobuj" + "ahmed") # overloading
print([10,20,30] + [40,50,60]) # overloading

# adding two object
print(sakib + mushi)

# multiplying two objects
print(sakib * mushi)

# subtracting two objects
print( sakib - mushi)

# checking greater object
print(sakib > mushi)
        