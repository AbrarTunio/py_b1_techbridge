class Car:
    wheels = 4

    def __init__(self , brand , color):
        self.brand = brand
        self.color = color

car1 = Car('Mehran' , 'White')
car2 = Car('Corolla' , 'Red')


print( car2.brand )

print( car2.wheels )

Car.wheels = 9


print( car1.wheels )