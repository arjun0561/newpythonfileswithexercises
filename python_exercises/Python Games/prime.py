n = int(input("Enter a number: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print(f"{n} is {'prime' if is_prime else 'composite'}.")