class Engine:
    def __init__(self):
        pass
    def start(self):
        print("car chalu")

# car "has an" engine
class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
    
jaguar = Car()
jaguar.start()