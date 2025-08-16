word = input("Enter a word: ").lower()

vowels = ["a", "e", "i", "o", "u"]

count = 0
for vowel in word:
    if vowel in vowels:
        count += 1

print(f"The number of vowels in the word is: {count}")

