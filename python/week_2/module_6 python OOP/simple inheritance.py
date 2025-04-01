"""
    Inheritance

    1. base class also known as parent class contains common data and methods
    2. derived class also known as child class contains uncommon data and methods

"""
# base class
class Gadget:
    def __init__(self,brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color
    
    def run(self):
        return f"running laptop: {self.brand}"

# derived class
class Laptop:
    def __init__(self, memory):
        self.memory = memory
    
    def coding(self):
        return f"coding in python"
    
# derived class
class Phone(Gadget):
    def __init__(self,brand, price, color, dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand, price, color)

    def phone_call(self, number, sms):
        return f"sending message: {sms} to {number}"
    def __repr__(self):
        return f"{self.brand} {self.price} {self.color}"

# derived class
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel
    
    def change_lens(self):
        pass
    
my_phone = Phone("samsung",10000,"golden",True)
print(my_phone)