name = input("Enter your name: ")

print(name)
print( type( name )   )

##################################
age = input( "Enter your age: " )

print(age )
print( type( age ) )

# PROBLEM IN CALCULATION FOR STRING NUMBERS
# Contacatenation 

num1 = "5"
num2 = "10"

print( int( num1 ) +  int( num2 ) )  #type conversion str into int

###########################################
a = input("Enter any number1")
b = input("Enter any number2")

print( int( a ) + int( b ) )

######################################
x =  int( input("how much amount do you have in pocket? ") )
y = int(  input("How much amount is in Sir Abrar's pocket")  )

total_amount = x + y

print( total_amount )

###############################
name = "Masharib "
copies = 5

print( name * copies  )