numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1} : "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)

print(f'The maximum of the data set is {maximum}')
print(f'The minimum of the data set is {minimum}')