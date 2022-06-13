# Creating the empty set
s = set()
print(type(s))
# Adding values to an empty set
s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.add((22, 33,334))
# s.add([1,3,2]) # Cannot add list to the set
# s.add({1:2}) # Cannot add dictionary to the set
print(s)

# Define length of the set
print(len(s))

# Remove element from existing set
s.remove(1)
print(s)
# Remove an orbitary element from the set and returns the element removed
s.pop()
print(s)
# empities the set
# s.clear()
# print(s)

# Return a new set with all items from both sets
print(s.union({5,7,6}))

# Return a set which contains only items in both sets

y = {1, 2, 5}
print(s.intersection(y))

