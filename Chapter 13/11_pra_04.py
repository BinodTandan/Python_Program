li = [2,5,10, 13, 15, 20, 25, 14, 77, 75, 80, 90]

a = lambda a: a%5==0

print(list(filter(a, li)))