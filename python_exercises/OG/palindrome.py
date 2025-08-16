word = input("Enter a word: ").lower()

reverse = word[::-1]
if word == reverse:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")