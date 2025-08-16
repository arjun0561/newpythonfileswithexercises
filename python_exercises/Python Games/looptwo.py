def sum_of_numbers():
    n = input("Enter a number: ")
    total = 0
    for i in range(1, int(n)):
        total += i
    return total

print(sum_of_numbers())
