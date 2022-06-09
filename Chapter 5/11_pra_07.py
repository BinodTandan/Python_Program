# If same key occur for multiple time than the first one give value and other not mentioned in the dictionary
s = {}
updateDict = { "Raju" : input("Enter 1st friend fav language: "),
    "Hari" : input("Enter 2nd friend fav language: "),
    "Raju" : input("Enter 3rd friend fav language: "), 
    "Laxman" :input("Enter 3rd friend fav language: ")
}
s.update(updateDict)

print(s)