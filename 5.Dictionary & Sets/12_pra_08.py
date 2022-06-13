# If the value of two keys are same than no change occurs in dictionary
s = {}
updateDict = { "Raju" : input("Enter 1st friend fav language: "),
    "Hari" : input("Enter 2nd friend fav language: "),
    "Ram" : input("Enter 3rd friend fav language: "),
    "Laxman" :input("Enter 3rd friend fav language: ")
}
s.update(updateDict)

print(s)