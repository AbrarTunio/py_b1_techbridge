std = {  'name' : 'Abrar' ,  
         'age' : 55   ,  
         'qualification' : 'ms',
         'city' : 'Hyderabad' 
      }

# for key in std:
#     print(key)

# for v in std.values():
#     print(v)

# for k , v in std.items():
#     print(k , '------->' , v)

print(std.keys())
print(std.values())

keys = list( std.keys() )
print( keys[2] )