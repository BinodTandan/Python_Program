
class Employee:
    status = "CEO"
    salary = 1900

binod = Employee()
raj = Employee()
binod.salary = 4000
raj.salary = 500

print(raj.salary)
print(binod.salary)
print(raj.status)
print(binod.status)
rahul = Employee.status = "Manager"
print(rahul)
