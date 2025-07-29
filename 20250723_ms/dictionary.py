student1 = { 
    "name" : "Abrar",
    "age" : 25.0,
    "degree" : "Matric Pass"
  }

student2 = { 
    "name" : "Masharib",
    "age" : 55.0,
    "degree" : "PHD",
  }

student2['name']  = 'Gorav'
student2['email'] = "Gorav@gmail.com"

for k , v in student2.items():
    print(k , v)