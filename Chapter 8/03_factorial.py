# n! = 1 * 2 * 3 * 4 * .......* n
# n! = n * (n-1)!

# n = 0
# product = 1
# for i in range(n):
#     product = product * (i+1)
# print(product)

# By using function



# Iteration Function

def factorial_iter(num):
    product = 1
    for i in range(num):
        product = product * (i+1)
    return product

result = factorial_iter(10)
print(result)


# Recursion 
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)

fact = factorial_recursive(1)
print(fact)


