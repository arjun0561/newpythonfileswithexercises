import random

secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to Guess the Number Game!")
print("Good luck guessing the number!")

while True:
    attempts += 1
    try:
        guess = int(input("Guess the number: "))
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        elif guess == secret_number:
            print(f"Congratulations! You have guessed the secret number {secret_number} correctly!")
            print(f"You took {attempts} attempts to guess the number.")
            break
    except ValueError:
        print("Invalid input. Please try again.")