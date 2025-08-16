import random

choices = ["rock", "paper", "scissors"]
def get_user_choice():
    while True:
        user_choice = input("Enter either rock, paper, or scissors: ")
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice, Please enter again.")

def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"
    
def play_game():
    print("Welcome to Rock Paper Scissors!")
    print("This is a game of 5 rounds. Good luck!")

    user_score = 0
    computer_score = 0
    round_num = 1

    while round_num <= 5:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            print("This round is a tie!")

        round_num += 1
        print(f"Updated Score | Your score: {user_score} | Computer Score: {computer_score}")

    print(f"----Final Results----")
    print(f"Your Score: {user_score} | Computer Score: {computer_score}")

    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("You lost. Better luck next time!")
    else:
        print("The game is a tie!")

play_game()