# 🔹 1. append()
# Adds an element to the end of the list.

# python
# Copy code
# fruits = ['apple', 'banana']
# fruits.append('orange')
# print(fruits)  # ['apple', 'banana', 'orange']
# 🔹 2. extend()
# Adds multiple elements to the end of the list.

# python
# Copy code
# fruits = ['apple']
# fruits.extend(['banana', 'mango'])
# print(fruits)  # ['apple', 'banana', 'mango']
# 🔹 3. insert(index, element)
# Inserts an element at a specific index.

# python
# Copy code
# fruits = ['apple', 'orange']
# fruits.insert(1, 'banana')
# print(fruits)  # ['apple', 'banana', 'orange']
# 🔹 4. remove(element)
# Removes the first matching element from the list.

# python
# Copy code
# fruits = ['apple', 'banana', 'apple']
# fruits.remove('apple')
# print(fruits)  # ['banana', 'apple']
# 🔹 5. pop(index)
# Removes and returns the element at the given index. If no index is provided, removes the last item.

# python
# Copy code
# fruits = ['apple', 'banana', 'orange']
# fruits.pop(1)
# print(fruits)  # ['apple', 'orange']
# 🔹 6. index(element)
# Returns the index of the first occurrence of the element.

# python
# Copy code
# fruits = ['apple', 'banana', 'orange']
# print(fruits.index('banana'))  # 1
# 🔹 7. count(element)
# Returns the number of times an element appears in the list.

# python
# Copy code
# numbers = [1, 2, 2, 3]
# print(numbers.count(2))  # 2
# 🔹 8. sort()
# Sorts the list in ascending order (modifies original list).

# python
# Copy code
# numbers = [3, 1, 2]
# numbers.sort()
# print(numbers)  # [1, 2, 3]
# 🔹 9. reverse()
# Reverses the order of elements in the list.

# python
# Copy code
# fruits = ['apple', 'banana', 'orange']
# fruits.reverse()
# print(fruits)  # ['orange', 'banana', 'apple']
# 🔹 10. copy()
# Returns a shallow copy of the list.

# python
# Copy code
# fruits = ['apple', 'banana']
# new_fruits = fruits.copy()
# print(new_fruits)  # ['apple', 'banana']
# 🔹 11. clear()
# Removes all elements from the list.

# python
# Copy code
# fruits = ['apple', 'banana']
# fruits.clear()
# print(fruits)  # []