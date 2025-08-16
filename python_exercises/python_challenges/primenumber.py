number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("The number is not a prime number.")
            break
    else:
        print("The number is a prime number.")
else:
    print("The number is not a prime number.")