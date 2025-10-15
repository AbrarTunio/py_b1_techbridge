# METHOD ONE

message = "techBridge"
print(message.capitalize())


# METHOD TWO - lower(), upper(), casefold()
greet = "SALAM"
print(greet.casefold())



# METHOD THREE
fruit = "WaterMelon"
print(fruit.count("e"))



# METHOD FOUR
sent = "A quick brown fox jumps over the lazy dog"
print(  len( sent )    )


# METHOD FIVE
letter = "Tech Bridge"
print( letter.endswith('dge')  )


# METHOD SIX
print(  letter.startswith( "tech" )   )  # Make sure about case sensitivity

# METHOD SEVEN
sent = "A q quick brown fo jumps over the lazy dog"
# print( sent.index('x')  )
print( sent.find('x')  )

# METHOD EIGHT
password = "abcd"
print( password.isalnum()  )


# METHOD NINE
password = "321316a"
print( password.isdigit()  )


# METHOD TEN
password = "321316a"
print( password.isnumeric()  )