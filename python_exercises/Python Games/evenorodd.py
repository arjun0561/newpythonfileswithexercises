def evenorodd():
    try:
        response = input("Enter a number so I can determine if it's even or odd: ")
        if int(response) <= 0:
            print('Please enter a positive integer')

        if int(response) % 2 == 0:
            print(f"{response} is an even number")
        elif int(response) % 2 != 0:
            print(f"{response} is an odd number")
    except ValueError:
        print("Please enter a valid number")

evenorodd()