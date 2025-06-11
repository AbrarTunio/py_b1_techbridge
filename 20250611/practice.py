# 1. Alien Language Decoder
# Write a program that takes a symbol (e.g. "@", "#", "$", "&", "*") as input and 
# prints its meaning in an alien language using elif. 
# Each symbol represents a different command like "run", "jump", "hide", etc.

# symbol = input ("Enter any symbol: ")

# if symbol == "@":
# 	print("run")
# elif symbol == "#":
# 	print("jump")
# elif symbol == "$":
# 	print("hide")
# else:
# 	print("I do not understand alien language")
	

# 2. Magic Door Selector
# Create a program where a user chooses a number between 1 to 5, 
# and based on the number, a different door opens revealing a magical place 
# (e.g., Dragon Cave, Candy Forest, Time Portal, etc.) using elif.

chosenNumber = input("Enter a number between 1 - 5: ") 

if chosenNumber == "1" or chosenNumber == "one":
	print("Dragon Cave")
elif chosenNumber == "2" or chosenNumber == "two":
	print("Candy Forest")
elif chosenNumber == "3" or chosenNumber == "three":
	print("Time Portal")
elif chosenNumber == "4" or chosenNumber == "four":
	print("No Man's Land")
elif chosenNumber == "5" or chosenNumber == "five":
	print("Lucky Irani Circus")
else:
	print("Not a number or not a number between 1-5")

# 3. Custom Pizza Maker
# Ask the user to enter a topping name (like "pepperoni", "mushroom", "pineapple", etc.). Based on the topping, display a unique description of the pizza they're getting. Use elif to handle the options.

# 4. Festival Finder by Month
# Prompt the user to input a month (as a number 1–12). Based on the month, display a major global festival or event using elif. Example: 12 = Christmas, 7 = Independence Day (USA), etc.

# 5. Robot Mood Interpreter
# Input the robot's mood as a word (e.g. "happy", "tired", "angry", "curious"). Based on the input, output a creative robot response using elif, like “initiating dance sequence” or “charging batteries.”