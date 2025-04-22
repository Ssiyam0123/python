class Animal:
    def __init__(self):
        print("Animal is created")
    def sound(self):
        print("Animal is making sound")
    def move(self):
        print("Animal is moving")
        
        
class Dog(Animal):
    pass

        
d = Dog()
d.sound()
d.move()
       