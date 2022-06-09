from functools import reduce


li = [12, 10 ,24, 55, 77, 88, 99]
# Method 1
# fun = lambda x, y: x if x>y else y
# res = (reduce(fun, li))
# print(res)

# Method 2
print(reduce(max, li))