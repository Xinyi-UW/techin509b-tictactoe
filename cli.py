# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

def display_board(board):
    for row in board:
        print(" ".join(cell if cell is not None else '-' for cell in row))
    print()

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    player = 'X'

    while winner is None:
        display_board(board)
        print(f"Player {player}'s turn")
        row = int(input("Enter row (0, 1, or 2): ")
        col = int(input("Enter column (0, 1, or 2): ")

        if board[row][col] is not None:
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = player
        winner = get_winner(board)
        player = other_player(player)

    display_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")
