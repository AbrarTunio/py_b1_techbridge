with open( "myfile.txt" , "a+" ) as fhandle:
    fhandle.write("I have got intelligent students")

    fhandle.seek(0)  # Move pointer to the beginning of the file

    output = fhandle.readlines() #this gives you string


    for x in output:
        print(x)
