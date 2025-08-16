import random

number = random.randint(1, 100)
guess = None

while guess != number:
    guess = int(input("Try to guess the number: "))
    if guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")
    else:
        print("You got it!")