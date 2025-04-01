# multi level inheritance = grandpa -> father -> child

class Vehicle:
    def __init__(self,name, price):
        self.name = name
        self.price = price

    def move(self):
        pass

    def __repr__(self):
        return f"{self.name} {self.price}"

class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        super().__init__(name, price)

    def __repr__(self):
        print(self.seat)
        return super().__repr__()   # calling its parents representation

# multi level inheritance
class AcBus(Bus):
    def __init__(self, name, price, seat, temp):
        self.temp = temp
        super().__init__(name, price, seat)

    def __repr__(self):
        print(self.temp)
        return super().__repr__()  #class it's parent representation

green_line = AcBus("green line", 10000000, 40, 25)
print(green_line)
        