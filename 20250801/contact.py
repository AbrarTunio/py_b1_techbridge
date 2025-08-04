contacts = {}

# Adding contacts
contacts["Abrar"] = "03001234567"
contacts["Bilal"] = "03111234567"

# Search
name = input("Enter name to search: ")
print("Number of", name , "is:",  contacts.get(name, "Not found"))
