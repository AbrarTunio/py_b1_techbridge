fhandle = open( "myfile.txt" , "w+" )

fhandle.write("I have got intelligent students")
output = fhandle.read() #this gives you string

for x in output:
    print(x)
