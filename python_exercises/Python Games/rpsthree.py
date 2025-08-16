import random

def play_game():
    player_score = 0
    computer_score = 0
    rounds_played = 0
    choices = ['rock', 'paper', 'scissors']

    print("Welcome to Rock, Paper, Scissors!")
    print("First to three rounds wins the game. Good luck!")

    while player_score < 3 and computer_score < 3:
        print(f"Current score:  You: {player_score} | Computer: {computer_score}")
        print(f"Your chances to win are: {calculate_win_percentage(player_score, rounds_played)}")

    user_choice = ""
    while user_choice not in choices:
        user_choice = input(f"Please enter either rock, paper, or scissors please.").lower()
        if user_choice not in choices:
            print("Please enter a valid choice")

    computer_choice = random.choice(choices)
    print(f"Your choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    rounds_played += 1

    if result == "player":
        print("You won this round!")
        print(f"Your win percentage: {calculate_win_percentage()}")
    elif result == "computer":
        print("The computer won the game.")
        print(f"Your win percentage: {calculate_win_percentage(player_score, rounds_played)}%")
    else:
        print("This round is a tie!")

    print("-") * 40

    print("\nGAME OVER!")
    print(f"Final score - You: {player_score} | Computer: {computer_score}")
    print(f"Rounds played: {rounds_played}")
    print(f"Your win percentage: {calculate_win_percentage()}")

    if player_score > computer_score:
        print("You win!")
    else:
        print("The computer won the game. Better luck next time.")

def calculate_win_percentage(wins, total_rounds):
    if total_rounds == 0:
        return 0.0
    print((wins / total_rounds) * 100, 2)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

play_game()

while True:
    play_again = input("Do you want to play this game again? (yes/no) : ").lower()
    if play_again == "yes":
        print("\nStarting game now...\n")
        play_game()
    elif play_again == "no":
        print("Thanks for playing!")
        break
    else:
        print("Please enter either yes or no.")
