from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.current_location = current_location
        self.wallet = initial_amount

    def display_profile(self):
        print(f"rider: {self.name}   email: {self.email}")

    def load_cash(self, amount: int):
        if amount > 0:
            self.wallet += amount
        else:
            print("amount is less than 0")
    
    def update_location(self, current_location: str) -> None:
        self.current_location = current_location
    
    def request_ride(self, ride_sharing, location):
        pass

    def show_current_ride(self):
        print(f"current ride: {self.current_ride}")

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0
    
    def display_profile(self):
        print(f"driver name: {self.name}")

    def accept_ride(self, ride):
        ride.set_driver = self
