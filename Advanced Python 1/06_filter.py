def gre_than_7(num):
    if num > 7:
        return True

    else:
        return False

g = lambda num: num>10
l = [1, 2, 8, 6, 9,22, 21, 55,]
print(list(filter(gre_than_7, l)))
print(list(filter(g, l)))