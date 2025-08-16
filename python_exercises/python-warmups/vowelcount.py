def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for char in text.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count

print(count_vowels("Hello World"))