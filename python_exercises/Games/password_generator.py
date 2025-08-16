import random
import string

def generate_password(length=100):
    if length < 8:
        length = 8  # Force minimum 8 characters
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(f"Generated Password: {generate_password()}")
