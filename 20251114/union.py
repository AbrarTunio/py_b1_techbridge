setA = { 5 , 9 , 8 , 7 }
# x = { 25 , 81, 64, 49 }
setB = { 5 , 6 , 8 , 11 }

x = setA | setB #union  { 5 , 9 , 8 , 7 , 5 , 6 , 8 , 11 } = { 5 , 9 , 8 , 6 , 11 }
y = setA.union(setB)
print(x)
print(y)

#-----------------------------------
print( setA & setB )
print( setA.intersection( setB ) )

#--------------------Differnece
print( setA.difference(setB) )
print( setA.symmetric_difference(setB) )


# ---------------------
# Membership test

if 13 in setA:
    print('Yes')
else:
    print('NO')


x = { x+2 for x in setA }
print(setA)
print(x)