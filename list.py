my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert an element at index 2
my_list.insert(1, 15)

print(my_list)

# extend the list with another list
my_list.extend([50, 60, 70])
print(my_list)

# remove elements by index
# my_list.pop(3)  # removes the element at index 3

# remove an element by value
my_list.remove(70)
print(my_list)

# sort the list
my_list.sort()
print(my_list)

# Find the index of an element
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")