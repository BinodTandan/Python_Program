def temperature(celsius):
    ferh = (celsius*9/5) + 32
    return ferh

temp = int(input("Enter temperature: "))
res = temperature(temp)
print(f"{temp} degree celsius is {res}")