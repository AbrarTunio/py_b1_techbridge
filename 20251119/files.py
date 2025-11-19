fhandle = open( "myfile.txt" , "r" )


output = fhandle.readlines() #this gives you list
output = fhandle.read() #this gives you string

fhandle.close()

print( output )
print( type(output)  )