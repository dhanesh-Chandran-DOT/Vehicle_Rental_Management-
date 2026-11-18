from Vehicle import Vehicle

class Car(Vehicle):
    def calculate_rent(self,days):
        rent = self.rental_price*days + 500
        print(rent)
    