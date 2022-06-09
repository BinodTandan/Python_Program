a = 10 # Global Variable
def fun2():
    global a
    print(a)
    a= 12 # Local Variable if global keyword is not used

    print(a)

fun2()
print(a)