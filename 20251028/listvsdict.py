student = [ 'Abrar' , '55' , 'MS' ]

print(student[1])

std = {  'name' : 'Abrar' ,  
         'age' : 55   ,  
         'qualification' : 'ms' 
      }

std['name'] = 'Masharib'

print(  std['name']  )     #method 1
print(  std.get('name') )  #method 2

# Adding new entry to dictionary
std['city'] = 'Hyderabad'



print(std)
