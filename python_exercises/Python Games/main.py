def multiplication():
    multi = input("What is 3 multiplied by 4? ")
    try:
        if int(multi) == 12:
            print("You got it correct!")
            return 1
        else:
            print("Sorry you got the question wrong. I am sure you can do better next time.")
            return 0
    except ValueError:
        print("Please enter a valid number.")
        return 0

def addition():
    add = input("What is 5 + 6? ")
    try:
        if int(add) == 11:
            print("You got the question correct!")
            return 1
        else:
            print("Sorry you got it wrong.")
            return 0
    except ValueError:
        print("Please enter a valid number.")
        return 0

def division():
    divide = input("What is 72 divided by 9? ")
    try:
        if int(divide) == 8:
            print("You got it correct! Thank you so much for completing the game!")
            return 1
        else:
            print("You got it wrong, but thank you so much for completing my game.")
            return 0
    except ValueError:
        print("Please enter a valid number.")
        return 0

def play_game():
    name = input("What is your name? ")
    print("Hello " + name)
    age = input("What is your age? ")

    try:
        if int(age) > 5:
            print("You are able to play this game.")
            print("This is a game of trivia which has three questions.")

            score = 0
            total_questions = 3

            score += multiplication()
            score += addition()
            score += division()

            percentage = (score / total_questions) * 100
            print(f"\n{name}, you got {score} out of {total_questions} questions correct.")
            print(f"Your score percentage is: {percentage:.2f}%")
        else:
            print("You are not able to play this game.")
    except ValueError:
        print("Please enter a valid age.")

# Main loop to allow replaying
while True:
    play_game()
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay not in ("yes", "y"):
        print("Thanks for playing! Goodbye!")
        break