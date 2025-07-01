def message(name):
	return "This is a secret message: " + name


user = input("Enter the name of message receiver: ")
msg = message(user)
print(msg)