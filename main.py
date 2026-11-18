from Car import Car
from Bike import Bike
from Vehicle import Vehicle

c = Car("BMW", 2400, 10000)
b = Bike("Pulsar", 2401, 5000)

 
c.calculate_rent(3)
b.calculate_rent(5)

c.display_details()
b.display_details()