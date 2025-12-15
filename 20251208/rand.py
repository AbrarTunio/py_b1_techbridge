import random
import os

# x = random.random()

# x = random.randint(1 , 10)

# x = random.randrange(1 , 11)

myfriends = ['Abrar' , 'Imran' , 'Suhail' , 'Masharib' , 'Huzoro'] 

# x = random.choice( myfriends )

# x = random.choices( myfriends , k=2 )

# random.shuffle( myfriends )

# print(myfriends)

x = random.choice(myfriends)

os.mkdir(x)

os.chdir(x)
fh = open('imran.txt' , 'x')   