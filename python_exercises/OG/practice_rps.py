import random

choices = ['rock', 'paper', 'scissors']
def get_user_choice():
    while True:
        user_choice = input("Choose either rock, paper, or scissors: ")
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid response. Enter again.")

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
    print("Welcome to Rock, Paper, Scissors!")
    print("This is a game of 5 rounds. Good luck!\n")

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
            print("It is a tie!")

        round_num += 1

        print(f"Updated Score | Your Score: {user_score} | Computer Score: {computer_score}")
    # Final Results
    print("----Final Results----")
    print(f"Final Score | Your Score: {user_score} | Computer Score: {computer_score}")

    print("Thanks for playing!")

play_game()