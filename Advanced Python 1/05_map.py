def square(num):
    return num*num
li = [1, 3, 4, 5]
#Method 1
# l1 = []
# for item in li:
#     l1.append(square(item))

# print(l1)
#Method 2
print(li)
print(list(map(square,li)))