import random

choices = ['rock', 'paper', 'scissors']
def get_user_choice():
    while True:
        user_choice = input("Choice rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice, please pick again.")

def get_computer_choice():
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie")
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    if winning_combinations[user_choice] == computer_choice:
        print("You win!")
    else:
        print("Computer wins!")

def play_game():
    print("Welcome to Rock Paper Scissors!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
    else:
        print("Restarting the game...")
        play_game()

play_game()