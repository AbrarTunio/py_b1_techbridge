list = list()  #this is an empty list

myList = [] # Empty list

general = [  "Imran" , 55 , True , []  ,  [ 'go' , 'gone' ]  ]

name = general[0]
emptyList = general[3]
nestedList = general[4]

# print(name)
# print(emptyList)
# print(nestedList[1])
# nestedListEntry = general[4][1]

nestedListEntry = general[-1][1]

# print(nestedListEntry)

# message = "I am in trouble"
# listMessage = message.split()

# print(message)
# print(listMessage)

# print(listMessage[2])
# print(listMessage[-2])

# dateList = [ '15' , 'Oct' , '2025' ]

# dateFormat = "-".join(dateList)
# print(dateFormat)

# print( dir(dateList)  )

fruits = ['Banana' , 'WaterMelon' , 'Apple' , 'Strawberry']

# fruits.append('Kiwi')
# fruits.insert( 2, 'Kiwi')
# fruits.add('kiwi')

# lastFruit = fruits.pop(1)

# print(fruits)
# print(lastFruit)

# fruits.remove("Apple") #Remove takes the entryname from list

# fruits.sort() # Do not store in variable - do directly to original
fruits.reverse()

print(fruits)


