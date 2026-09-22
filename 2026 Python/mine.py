class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def get_info(self): 
        print(f"Brand: {self.brand}, Price: {self.price} $")

class ElectricCar(Car):
    def __init__(self, brand, price, battery):
        super().__init__(brand, price)
        self.battery = battery
        
    def get_info(self):
        print(f"Electrocar: {self.brand}, Price: {self.price} $, Battery: {self.battery} km")

regular_car = Car("Kia Sorento", 60000)
ev_car = ElectricCar("Deepal S09", 50000, 215)

regular_car.get_info()
ev_car.get_info()