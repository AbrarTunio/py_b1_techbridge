class Car:

    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def showbrand( self ):
        print( f"The brand of my car is: {self.brand}" )

car = Car('Honda Atlas')
car.showbrand()