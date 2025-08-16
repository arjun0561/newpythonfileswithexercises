def is_palindrome(text):
    text = str()
    reverse = text[::-1]
    if text.lower() == reverse:
        return "This word is a palindrome."
    else:
        return "This word is not a palindrome."

print(is_palindrome("rACeCar"))