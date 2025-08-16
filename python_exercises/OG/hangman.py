import random

words = ['monkey', 'donkeys', 'python', 'programming', 'hangman']
word = random.choice(words)
guesses = ""
turns = 17

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print('_', end=" ")
            failed += 1
    if failed == 0:
        print("\nYou win!")
        break
    guess = input("\nGuess a letter: ").lower()
    guesses += guess
    if guess not in word:
        turns -= 1
        print(f"Wrong! Number of turns left: {turns}")