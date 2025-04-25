class Car:
    def __init__(self, userBrand, userModel):
       self.brand = userBrand
       self.model = userModel
       
    def fullName(self):
        return f"{self.brand} {self.model}" 
    
    
    
class ElectricCar(Car):
    def __init__(self, userBrand, userModel, batterySize):
        super().__init__(userBrand, userModel)
        self.batterySize = batterySize
        
        

my_tesla = ElectricCar("tesla", 'model s', '85kwh')
print(my_tesla.batterySize)        
             
    
# my_car = Car("toyota", "corola")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())


# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)