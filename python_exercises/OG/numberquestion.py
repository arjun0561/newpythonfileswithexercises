import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    attempts += 1
    try:
        guess = int(input("Guess the number: "))
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        elif guess == secret_number:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"You took {attempts} attempts to guess the number.")
            break
    except ValueError:
        print("Invalid input. Please try again.")

print("Thanks for playing!")
