from Car import Car     # import car,bike,vehicle classes from their files
from Bike import Bike
from Vehicle import Vehicle

c = Car("BMW", 2400, 10000)     # creating car object name = bmw, vehicle number = 2400, price = 10000
b = Bike("Pulsar", 2401, 5000)  # creating  bike object name = pulsar, vehicle number = 2401, price = 5000

 
c.calculate_rent(3)     # car rent for 3 days = 10000*3 + 500 = 30500
b.calculate_rent(5)     # bike rent for 5 days = 5000*5 + 100 = 25100

c.display_details()      # displays the details of car object c
b.display_details()      # displays the details of bike object b