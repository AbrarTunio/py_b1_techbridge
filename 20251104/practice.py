# # person = {
# #     'name' : 'Masharib',
# #     'age' : 19,
# #     'country' : 'Italy'
# # }

# # print( person['name'] )
# # print( person['age'] )
# # print( person['country'] )


# # person['email'] = 'abrar.tunio@yahoo.com'
# # person['country'] = 'Pakistan'

# # x = person.pop('age')
# # print(x)
# # person.clear()
# # print(person)





# students = {
#     'honey' : 55,
#     'bunny' : 15,
#     'money' : 99,
#     'funny' : 62,
#     'sunny' : 10
# }

# for k , v in students.items():
#     if v >= 20:
#         print( k , v , 'pass' )
#     else:
#         print( k , v , 'fail' )

string = 'A quick quick brown fox jumps over the lazy dog'
listOfWords = string.split()

count = {}

# count['A'] = 1

for word in listOfWords:
    if word not in count:
        count[word] = 1
    else:
        count[word] += 1

print(count)