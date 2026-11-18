from abc import ABC ,abstractmethod

class Vehicle(ABC):
    def __init__(self,name,vehicle_no,price):
          self.name = name
          self.vehicle_no = vehicle_no
          self.__price = price              #rental price


    @abstractmethod
    def calculate_rent(self):
            pass

    @property
    def rental_price(self):
         return self.__price
                  

    def display_details(self):
        print("name of the vehicle:",self.name)
        print("vehicle number is :",self.vehicle_no)
        print("price of the vehicle is :",self.rental_price)
