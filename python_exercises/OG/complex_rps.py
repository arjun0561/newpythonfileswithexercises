import random

def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if winning_combinations[user_choice] == computer_choice:
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("We'll play 5 rounds. Let's see who wins!\n")
    
    user_score = 0
    computer_score = 0
    round_num = 1
    
    while round_num <= 5:
        print(f"--- Round {round_num} ---")
        print(f"Current Score - You: {user_score} | Computer: {computer_score}\n")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        
        if result == "user":
            user_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")
        
        round_num += 1
        print(f"Updated Score - You: {user_score} | Computer: {computer_score}\n")
    
    # Determine final winner
    print("\n--- Final Results ---")
    print(f"Your score: {user_score} | Computer score: {computer_score}")
    
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > user_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")
    
    print("\nThanks for playing!")

# Start the game
play_game()