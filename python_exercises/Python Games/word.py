def numberofvowelsandconsonants():
    word = input("Enter a word: ").lower()  
    
    vowels = 0
    consonants = 0
    
    vowel_letters = {'a', 'e', 'i', 'o', 'u'}
    
    for char in word:
        if char.isalpha():  
            if char in vowel_letters:
                vowels += 1
            else:
                consonants += 1
    
    print(f"\nWord: {word}")
    print(f"Number of vowels: {vowels}")
    print(f"Number of consonants: {consonants}")

numberofvowelsandconsonants()