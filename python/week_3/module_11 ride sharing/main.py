from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Driver, Rider
from vehicle import Car, Bike

pathao = RideSharing("pathao")
rohim = Rider("rohim", "rohim@gmail.com", 15482, "mirpur", 200)
pathao.add_rider(rohim)

korim = Driver("korim", "korim@gmail.com", 58768, "dhanmondi")
pathao.add_driver(korim)

rohim.request_ride(pathao, "dhanmondi", "bike")
rohim.show_current_ride()

korim.reach_destination(rohim.current_ride)

print(pathao)
