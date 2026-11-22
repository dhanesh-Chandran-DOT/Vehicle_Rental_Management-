from Vehicle import Vehicle # brings the base class from vehicle.py

class Car(Vehicle):         # inheritance ,car gets everything from vehicle
    def calculate_rent(self,days):  #polymorphism ,same method also in vehicle also
        rent = self.rental_price*days + 500 # fromula for car to find rental price per days 
        print(rent)                 # print the total rent
    