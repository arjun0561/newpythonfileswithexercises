import random

words = ['python', 'banana', 'school']
word = random.choice(words)
scrambled_word = "".join(random.sample(word, len(word)))

chances = 3

print("Welcome to the Word Scramble Game!")
print(f"This is the scrambled word: {scrambled_word} | Try to guess what word it is. Good Luck!")
while chances > 0:
    guess = input("Guess the word: ").lower()
    chances -= 1
    if guess == word:
        print("You got it! Good job!")
        break
    elif guess != word:
        print(f"Wrong! Try again. You have {chances} chances left.")
    else:
        print(f"You are out of tries. The word was {word}.")
        break