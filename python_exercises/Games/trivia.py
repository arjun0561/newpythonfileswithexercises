def addition():
    while True:
        try:
            add = int(input("What is 5 + 6? "))
            if add == 11:
                print("You got it!")
                break
            else:
                print("Wrong. Try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def subtraction():
    while True:
        try:
            subtract = int(input("What is 69 - 49? "))
            if subtract == 20:
                print("You got it!")
                break
            else:
                print("Wrong. Try again.")
        except ValueError:
            print("Invalid input. Please try again.")        

def multiplication():
    while True:
        try:
            multiply = int(input("What is 23 * 43? "))
            if multiply == 989:
                print("You got it!")
                break
            else:
                print("Wrong. Try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def division():
    while True:
        try:
            divide = int(input("What is 121 / 11? "))
            if divide == 11:
                print("You got it!")
                break
            else:
                print("Wrong. Try again.")
        except ValueError:
            print("Invalid input. Please try again.")

def play_trivia():
    print("Welcome to this Math Trivia!\n Good luck!")
    addition()
    subtraction()
    multiplication()
    division()
    print("\nThanks for playing!\n")

play_trivia()
