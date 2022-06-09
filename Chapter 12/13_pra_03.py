
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# a = int(input("Enter a number: \n"))
# li2 = [i for i in li if i%a==0]
# print(li2)
while(True):
    num= int(input("Enter a number: "))
    table = [num*i for i in range(1,11)]
    print(table)
