from abc import ABC ,abstractmethod         # ABC is imported ro make an abstract class

class Vehicle(ABC):                         # parent class
    def __init__(self,name,vehicle_no,price): # init -sets the name and price 
          self.name = name
          self.vehicle_no = vehicle_no
          self.__price = price              # this is encapsulation(private) , no one can access price directly from outside.


    @abstractmethod                          #  This is Abstraction
    def calculate_rent(self):
            pass

    @property                                 # This gives safe read-only access to the private price. This is also Encapsulation.
    def rental_price(self):
         return self.__price
                  

    def display_details(self):                  # This prints the details
        print("name of the vehicle:",self.name)
        print("vehicle number is :",self.vehicle_no)
        print("price of the vehicle is :",self.rental_price)
