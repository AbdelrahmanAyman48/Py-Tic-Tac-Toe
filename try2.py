import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to make a move for the computer
def computer_move(board, computer_char, player_char):
    # Check for winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = computer_char
                if check_winner(board, computer_char):
                    return
                else:
                    board[i][j] = " "

    # Check for blocking move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player_char
                if check_winner(board, player_char):
                    board[i][j] = computer_char
                    return
                else:
                    board[i][j] = " "

    # Choose a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = computer_char
            return

# Function to play the Tic Tac Toe game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_char = input("Choose X or O: ").upper()
    computer_char = "O" if player_char == "X" else "X"

    while True:
        print_board(board)
        if player_char == "X":
            player_move = input("Enter your move (row col): ").split()
            row, col = int(player_move[0]), int(player_move[1])
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = player_char
        else:
            computer_move(board, computer_char, player_char)

        if check_winner(board, player_char):
            print_board(board)
            print("You win!")
            break
        elif check_winner(board, computer_char):
            print_board(board)
            print("Computer wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

# Main function to start the game
if __name__ == "__main__":
    play_game()
