import random

def play_game():
    # Initialize scores
    player_score = 0
    computer_score = 0
    rounds_played = 0
    choices = ['rock', 'paper', 'scissors']
    
    print("Welcome to Rock, Paper, Scissors!")
    print("First to win 3 rounds wins the game!\n")
    
    while player_score < 3 and computer_score < 3:
        print(f"Current Score - You: {player_score} | Computer: {computer_score}")
        print(f"Win Percentage: {calculate_win_percentage(player_score, rounds_played)}%")
        
        # Get user input with validation
        user_choice = ""
        while user_choice not in choices:
            user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
            if user_choice not in choices:
                print("Invalid choice. Please enter rock, paper, or scissors.")
        
        # Computer makes random choice
        computer_choice = random.choice(choices)
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine round winner
        result = determine_winner(user_choice, computer_choice)
        rounds_played += 1
        
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("This round is a tie!")
        
        print("-" * 40)
    
    # Game over - display final results
    print("\nGAME OVER!")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")
    print(f"Rounds Played: {rounds_played}")
    print(f"Your Win Percentage: {calculate_win_percentage(player_score, rounds_played)}%")
    
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    else:
        print("Computer won the game. Better luck next time!")

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

def calculate_win_percentage(wins, total_rounds):
    if total_rounds == 0:
        return 0.0
    return round((wins / total_rounds) * 100, 2)

# Start the game
play_game()

# Ask to play again
while True:
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        print("\nStarting a new game...\n")
        play_game()
    elif play_again == 'no':
        print("Thanks for playing!")
        break
    else:
        print("Please enter 'yes' or 'no'.")