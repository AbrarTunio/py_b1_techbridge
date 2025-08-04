scores = { }

scores["Ali"] = 90
scores["Sara"] = 85

# Add new score
for count in range(6):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    scores.update({name: marks})

# Show all results
for name, mark in scores.items():
    print(name, "got", mark)
