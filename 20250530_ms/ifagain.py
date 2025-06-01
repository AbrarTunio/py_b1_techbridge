# age = int( input("How old are you?  ") )

# if age >= 90:
# 	print("You are about to die")
# elif age >= 18:
# 	print("You are eligible to vote ")
# elif age < 18:
# 	print("You are too young")

# pocketMoney = int( input("How much do you have? "))

# if pocketMoney > 1000:
# 	print("Let's do BBQ")
# elif pocketMoney < 1000:
# 	print("Save your money")
# else:
# 	print("Just about 1000")

age = 30
citizen = False

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Too young to vote")
