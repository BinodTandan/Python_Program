myDict = { "Kam Garni" : "Working",
            "Khelni" : "Playing",
            "Padni": "Studying",
            "Hidni" : "Walking",
            "Maya" : "Love"
}

print("Options are:", myDict.keys())
a = input("Enter the Nepali Word:\n")
print("The meaning of your word is:",myDict.get(a))
