class Math:

    def __init__(self , x):
        self.x = x

    def showx(self):
        return self.x 
    
    def square(self):
        return self.x * self.x

obj = Math(5)
print( obj.showx() )
print( obj.square() )
