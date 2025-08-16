def count_vowels():
    word = input("Enter a word: ").lower()
    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0
    for char in word:
        if char in vowels:
            count += 1
        
    print(f"The number of vowels in the word {word} is {count}.")

count_vowels()