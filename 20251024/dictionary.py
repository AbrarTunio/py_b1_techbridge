dictionary = {  }
# myDict = dict()


car = { 
    "brand" : "Toyota",
    'model' : "Corola",
    'year'  : 2005
}

print(car['brand'])

car['brand'] = 'Mercedes' # Modify or update
car['color'] = 'black'    # Insert new

print(car['brand'])

del( car['color'] )       # Delete Existing
print(car)

print(car.items())

for key , value in car.items():
    print(key , 'is' , value)
