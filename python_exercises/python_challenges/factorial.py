number = input("Enter a number: ")

factorial = 1

for i in range(1, int(number) + 1):
    factorial *= i

print(f"The factorial of {number} is {factorial}.")