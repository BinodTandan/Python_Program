a =[1,  10,66, 77, 42, 98, 9, 3, 12, 14, 17, 119]
# # b = []
# # c = []
# # for item in a:
# #     if item%2==0:
# #         b.append(item)
# #     else:
# #         c.append(item)
# print(b)
# print(c)
# Shortcut of above code
b = [i for i in a if i%2==0]
c = [i for i in a if i%2!=0]
print(b)
print(c)

t = [1,2,3,2,34,4,2, 3,1,2]
s = {i for i in t}
print(s)