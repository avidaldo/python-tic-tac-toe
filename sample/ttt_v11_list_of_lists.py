"""
Resolución siguiendo estrictamente el enunciado de https://edube.org/learn/pe-1/project-tic-tac-toe-4
"""

from random import randrange


def display_board(board):
    def cell_display(row, col):
        return board[row][col] if (board[row][col] == "X" or board[row][col] == "O") else 3 * row + col + 1

    print("+------+------+------+")
    for row in range(3):
        print("|      |      |      |")
        print("|  ", cell_display(row, 0), " |  ", cell_display(row, 1), " |  ", cell_display(row, 2), " |")
        print("|      |      |      |")
        print("+------+------+------+")


def cell_to_row_col(cell):
    return (cell - 1) // 3, (cell - 1) % 3


def enter_move(board):
    while True:
        cell = input("Enter your move: ")
        if not (cell.isdigit() and int(cell) in range(1, 10)):
            print("You must enter a number (1-9).")
            continue
        row, col = cell_to_row_col(int(cell))
        if board[row][col] is not None:
            print("Invalid move, try again.")
        else:
            break
    row, col = cell_to_row_col(int(cell))
    board[row][col] = "O"


def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]


def victory_for(board, sign):
    if (# Filas
            board[0][0] == board[0][1] == board[0][2] == sign or
            board[1][0] == board[1][1] == board[1][2] == sign or
            board[2][0] == board[2][1] == board[2][2] == sign or
        #Columnas
            board[0][0] == board[1][0] == board[2][0] == sign or
            board[0][1] == board[1][1] == board[2][1] == sign or
            board[0][2] == board[1][2] == board[2][2] == sign or
        # Diagonales
            board[0][0] == board[1][1] == board[2][2] == sign or
            board[0][2] == board[1][1] == board[2][0] == sign):
        return True


def draw_move(board):
    if len(make_list_of_free_fields(board)) == 9:  # First move
        board[1][1] = "X"
        return
    list_of_free_fields = make_list_of_free_fields(board)
    row, col = list_of_free_fields[randrange(len(list_of_free_fields))]
    board[row][col] = "X"


def main():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while True:
        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("I won!")
            break
        if len(make_list_of_free_fields(board)) == 0:  # Draw only posible after X's move (X always moves first)
            print("Draw!")
            break
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("You won!")
            break


if __name__ == "__main__":
    main()
