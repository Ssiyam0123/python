# #basic syntax

# class ClassName:
#     pass

# class Student:
#     pass

# s1 = Student()



# # print(type(s1))

# class MyClass:
#     def __init__(self):
#         self.name = "Siyam"
#     def greet (self):
#         return "Hello"

# print(dir(MyClass))        



# a = MyClass()

# print(a.name)




# class Car :
#     def __init__(self,band,color):
#         self.band = band
#         self.color = color
    
#     def start_engine(self):
#         print(f"{self.band} engine started")
        
        

# myCar = Car("Honda", "Blue")

# myCar.start_engine()        
            
            


class Animal:
    def __init__(self, eye_color, weight, type):
        self.eye_color = eye_color
        self.weight = weight
        self.type = type

    def sound(self):
        print(f"This animal's eye color is {self.eye_color}, its weight is {self.weight}, and it is a {self.type} type animal.")


my_animal = Animal("red", "60kg", "dog")
my_animal.sound()

 
                        
            