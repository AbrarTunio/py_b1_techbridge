units = int(input("Enter Number of Units"))

if units >= 1 and units <= 100 :
	total = units * 5
	print(total, "=>" , units)
elif units >= 100 and units <= 200:
	totalOne = 100 * 5
	print(totalOne, "=>" , 100)
	totalTwo = (units - 100)*8
	print(totalTwo, "=>" , (units - 100) )
	total = totalOne + totalTwo
	print(total, "=>" , units)
elif units >= 200:
	rUnits = units
	totalOne = 100 * 5
	print(totalOne, "=>" , 100 )
	rUnits = rUnits - 100
	totalTwo = (rUnits - 100) * 10
	print(totalTwo , "=>" ,(rUnits - 100) ,"For 10 per units ")
	totalThree = 100 * 8
	print(totalOne+totalTwo+totalThree)