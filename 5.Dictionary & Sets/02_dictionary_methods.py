mydict = {
    "hello" : "World",
    "politic" : "Balen Shah",
    "sports" : ['Football','Cricket', 'Hockey'],
    "anotherdict" : {"Loyality" : "Binod"},
    1 : 2
}

# Methods in Dictonary
print(mydict.keys()) # Print the keys of dictonary
# print(list(mydict.keys())) # Convert dictionary into list
print(mydict.values())
print(mydict.items()) # Print the (key, value) for all contents in dictonary
updateDict = {
    "Binod" : "Tandan",
    "Gulmi" : "Charpala",
    "politic" : "Dirty Game"
}
mydict.update(updateDict)
print(mydict)

print(mydict["hello"])
print(mydict.get("hello"))

# The difference between .get and [] syntax
print(mydict["hello1"]) # throws an error as hello1 is not present in the dictionary
print(mydict.get("hello1")) # Return None as hello1 is not present in the dictionary

