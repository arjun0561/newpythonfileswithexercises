import random

choices = ['rock', 'paper', 'scissors']
def get_user_choice():
    while True:
        user_choice = input("Enter either rock, paper, or scissors: ")
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid input. Enter either rock, paper, or scissors.")

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
    print("Welcome to Rock Paper Scissors! ")
    print("We will play 5 rounds. Good luck!")

    user_score = 0
    computer_score = 0
    round_num = 1

    while round_num <= 5: 
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice} | Computer chose: {computer_choice}\n")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            print("It's a tie!")

        round_num += 1
        print(f"\nUpdated Score | Your Score: {user_score} | Computer Score: {computer_score}")

    print("----Final Results----")
    print(f"Your Score: {user_score} | Computer Score: {computer_score}")

    if user_score > computer_score:
        print("You won the game!")
    elif computer_score > user_score:
        print("You lost. Better luck next time.")
    else:
        print("The game is a tie!")

play_game()