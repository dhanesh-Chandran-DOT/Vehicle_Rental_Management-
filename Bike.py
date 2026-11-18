
from Vehicle import Vehicle



class Bike(Vehicle):
    def calculate_rent(self,days):
         rent = self.rental_price*days + 100
         print(rent)