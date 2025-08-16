import random

secret_number = random.randint(1, 50)
attempts = 0

run = True
while run:
    try:
        attempts += 1
        guess = int(input("Guess the secret number: "))
        if guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        elif guess == secret_number:
            print("You got it! Thanks for playing!")
            break
    except ValueError:
        print("Please enter an actual integer to guess the secret number.")

print(f"You took {attempts} attempts to guess the secret number {secret_number}.")