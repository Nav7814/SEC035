sum = 0
print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    sum += num
print(f"\nThe sum of the 10 numbers is: {sum}")
