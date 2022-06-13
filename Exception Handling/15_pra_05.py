num= int(input("Enter a number: "))
table = [num*i for i in range(1,11)]
res = print(f"The table of {num} = {table}") 
with open("table.txt", 'a') as f:
    f.write(str(table))
    f.write("\n")
