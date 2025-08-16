def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if board[0][0] == board[1][1] == board[2][2] == player: return True
    if board[0][2] == board[1][1] == board[2][0] == player: return True
    return False

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    try:
        print_board(board)
        row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print(f"Player {current_player} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken!")
    except ValueError:
        print("Not enough values to unpack.")