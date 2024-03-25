num1 = int(input("Enter the number for which you want the multiplication table:"))
lim = int(input("Enter the limit up to which you want the multiplication table generated:"))

print(f"Multiplication table for {num1}:")


for i in range(1, lim+1):
    print(f"{num1} x {i} = {num1 * i}")