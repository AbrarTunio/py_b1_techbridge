fh = open( 'myfile.txt' , 'r' )
# print( fh )
qty = {}
for letter in fh.read():
    if letter not in qty:
        qty[letter] = 1
    else:
        qty[letter] += 1    

print( qty )