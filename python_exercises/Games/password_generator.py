# import random

# def password_generator():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#     symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", '[', ']', "{", "}", "-", "_", "+", "=", "|", "?", "/", ":", ";", "<", ">", ",", "."]
#     uppercase_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", 'Z']
#     lowercase_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", 'z']
#     random_password = random.choice(numbers, symbols, uppercase_chars, lowercase_chars)
#     if len(random_password) <= 8:
#         return "Bad Password"
#     elif len(random_password) > 8:
#         return "Good password"
    
#     print(random_password)

# password_generator()

import random
import string

def generate_password(length=100):
    if length < 8:
        length = 8  # Force minimum 8 characters
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(f"Generated Password: {generate_password()}")