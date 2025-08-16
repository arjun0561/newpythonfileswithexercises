import random

secret_number = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number: "))
        if guess > secret_number:
            print("Too high. Try again!")
        elif guess < secret_number:
            print("Too low! Try again!")
        elif guess == secret_number:
            print("You got it!")
            break
    except ValueError:
        print("Please enter an actual number.")