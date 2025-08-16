import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    attempts += 1
    try:
        guess = int(input("Guess the number: "))
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        elif guess == secret_number:
            print("You got it!")
            break
    except ValueError:
        print("Invalid input. Try again.")

print(f"You guessed the secret number {secret_number} correctly!")
print(f"You took {attempts} attempts to guess the secret number.")