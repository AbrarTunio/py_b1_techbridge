# print("Num | x | Table | Result")
# print('------------------')
# for num in range(1,11):
# 	print(f'{num}   | x | 5 | {num * 5}')
# 	print('------------------')


for idx in range(1,11):
	userInput = input("Write #close to break the loop and #cont to continue")
	if userInput == '#close':
		print(idx, "breaking now")
		break
	if userInput == '#cont':
		print(idx, "Going Above")
		continue
