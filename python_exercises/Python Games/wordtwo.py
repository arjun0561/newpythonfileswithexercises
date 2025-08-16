def vowelsandconsonants():
    wordtwo = input("Enter your word: ").lower()

    vowels = 0
    consonants = 0

    vowel_letters = {'a', 'e', 'i', 'o', 'u'}

    for char in wordtwo:
        if char.isalpha():
            if char in vowel_letters:
                vowels += 1
            else:
                consonants += 1
    print(f"\nWord: {wordtwo}")
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

vowelsandconsonants()