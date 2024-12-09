"""
Defino el tablero de juego como un diccionario donde cada clave identifica el número que se mostrará para
identificar la casilla. Los valores de cada clave son None cuando no hay ficha y las contantes MACHINE y HUMAN cuando
hay una ficha de la máquina o del humano respectivamente.
"""

from random import choice

MACHINE = "X"
HUMAN = "O"


# ------------------------------ Lógica ------------------------------

def is_taken_cell(board, cell):
    return board[cell] is not None


def list_of_free_fields(board):
    return [i for i in range(1, 10) if not is_taken_cell(board, i)]


def is_first_move(board):
    return len(list_of_free_fields(board)) == 9


def is_board_completed(board):
    return len(list_of_free_fields(board)) == 0


WINNING_COMBINATIONS = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
    (1, 5, 9), (3, 5, 7)              # Diagonals
]

def victory_for(board, sign):
    return any(all(board[cell] == sign for cell in combination) for combination in WINNING_COMBINATIONS)


def machine_move(board):
    if is_first_move(board):
        board[5] = MACHINE
        return
    board[choice(list_of_free_fields(board))] = MACHINE


# ------------------------------ UI ------------------------------

_ENTER_MOVE_INPUT = "Enter your move: "
_INVALID_INPUT_MSG = "You must enter a number of a cell (1-9)."
_INVALID_MOVE_MSG = "That cell is already taken."
_YOU_WON = "You won!"
_DRAW = "Draw!"
_I_WON = "I won!"


def display_board(board: dict):
    def cell_display(cell):
        return board[cell] if is_taken_cell(board, cell) else cell

    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", cell_display(1), " |  ", cell_display(2), " |  ", cell_display(3), " |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", cell_display(4), " |  ", cell_display(5), " |  ", cell_display(6), " |")
    print("|      |      |      |")
    print("+------+------+------+")
    print("|      |      |      |")
    print("|  ", cell_display(7), " |  ", cell_display(8), " |  ", cell_display(9), " |")
    print("|      |      |      |")
    print("+------+------+------+")


def enter_move(board):
    while True:
        cell_str = input(_ENTER_MOVE_INPUT)
        try:
            cell = int(cell_str)
            if cell < 1 or cell > 9:
                print(_INVALID_INPUT_MSG)
            elif is_taken_cell(board, cell):
                print(_INVALID_MOVE_MSG)
            else:
                break
        except ValueError:
            print(_INVALID_INPUT_MSG)
    board[int(cell)] = HUMAN


def main():
    board = {i: None for i in range(1, 10)}

    while True:
        machine_move(board)
        display_board(board)
        if victory_for(board, MACHINE):
            print(_I_WON)
            break
        if is_board_completed(board):  # Draw only posible after X's move (X always moves first)
            print(_DRAW)
            break
        enter_move(board)
        display_board(board)
        if victory_for(board, HUMAN):
            print(_YOU_WON)
            break


if __name__ == "__main__":
    main()
