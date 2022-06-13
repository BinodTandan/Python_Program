num = 7
li = [str(num*i) for i in range(1,11)]
#Method 1
# for index, items in enumerate(li):
#     print(items)

#Method 2
verticalTable = "\n".join(li)
print(verticalTable)