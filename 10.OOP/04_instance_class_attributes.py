
class Employee:
    status = "CEO"
    salary = 1900

binod = Employee()
raj = Employee()
#Creating instance attributes
binod.salary = 4000
raj.salary = 500

print(raj.salary)
print(binod.salary)
print(raj.status)
print(binod.status)
# THrows an error below the line as age is not defined attribute in the class employee

# print(raj.age)
