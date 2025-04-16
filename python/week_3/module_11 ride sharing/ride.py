from datetime import datetime
from vehicle import Car, Bike

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider: object):
        self.riders.append(rider)
    def add_driver(self, driver: object):
        self.drivers.append(driver)
    
    def __str__(self):
        return f"company name: {self.company_name} with {len(self.riders)} riders and {len(self.drivers)} drivers and {len(self.rides)} total rides"

class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
    
    def calculate_fare(self, vehicle_type):
        distance = 10
        fare = {
            "car" : 50,
            "bike" : 30,
            "cng" : 35
        }
        return fare[vehicle_type] * distance

    def __repr__(self):
        return f"ride started from {self.start_location} to {self.end_location}"
    
class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers
    
    def find_driver(self, ride_request, vehicle_type):
        if len(self.available_drivers):
            print("drivers: ")
            driver = self.available_drivers[0]

            if vehicle_type == "car":
                vehicle = Car("car", "ab4587", 50)
            elif vehicle_type == "bike":
                vehicle = Bike("bike", "fds5844", 30)

            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
            driver.accept_ride(ride)
            return ride
    
    