def measurement(inches):
    cm = 2.54 * inches
    return cm

user = float(input("Enter specific inches: "))
print(measurement(user))