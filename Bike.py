
from Vehicle import Vehicle     # This brings the base class from Vehicle.py



class Bike(Vehicle):            # this is inheritance, bike is getting all the features of vehicle- like name,price.
    def calculate_rent(self,days):  # polymorphism ,same method also in vehicle also
         rent = self.rental_price*days + 100    # formula for bike 
         print(rent)                #prints the total rent