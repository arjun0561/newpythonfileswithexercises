import random

def number_generator(x, y):
    random_number = random.randint(x, y)
    print(random_number)

number_generator(1, 10000000000000)