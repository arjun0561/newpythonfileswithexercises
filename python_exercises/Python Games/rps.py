import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors")
    
    # Valid choices
    choices = ['rock', 'paper', 'scissors']
    
    # Get user input
    user_choice = input("Your choice: ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Your choice: ").lower()
    
    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()

# Optional: Ask if player wants to play again
while True:
    play_again = input("Play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_game()
    elif play_again == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Please enter 'yes' or 'no'.")