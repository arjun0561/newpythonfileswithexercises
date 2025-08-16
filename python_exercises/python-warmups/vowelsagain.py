def count_vowels():
    word = input("Enter a word: ").lower()

    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for char in word:
        if char in vowels:
            vowel_count += 1

    print(f"Number of vowels in {word}: {vowel_count}")

count_vowels()