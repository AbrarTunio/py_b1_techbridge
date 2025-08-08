import csv

data = [
    ["Name", "Age", "City"],
    ["Ali", 23, "Karachi"],
    ["Sara", 25, "Lahore"],
    ["Gorav", 30, "Islamabad"]
]


with open("myfile.csv", mode="w", newline="") as file:
    a = csv.writer(file)
    a.writerows(data)
    
with open('myfile.csv' , mode='r' ) as file:
    words = file.read()
    print(words)


