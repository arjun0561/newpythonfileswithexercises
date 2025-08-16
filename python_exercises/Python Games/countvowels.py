def count_vowels():
    word = input("Enter a word: ")

    vowels = 0

    vowel_letters = ['a', 'e', 'i', 'o', 'u']

    for char in word:
        if char.isalpha():
            if char in vowel_letters:
                vowels += 1

    print(f"Your word: {word}")
    print(f"\nNumber of vowels: {vowels}")

count_vowels()