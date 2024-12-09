"""
Defino el tablero de juego como un diccionario donde cada clave identifica el número que se mostrará para identificar la casilla. Los valores de cada clave son None cuando no hay ficha y las contantes MACHINE y HUMAN cuando hay una ficha de la máquina o del humano respectivamente.
"""

from random import choice

MACHINE = "X"
HUMAN = "O"

# ------------------------------ Lógica ------------------------------

def is_taken_cell(board, cell):
    return board[cell] is not None


def list_of_free_cells(board):
    return [i for i in range(1, 10) if not is_taken_cell(board, i)]


def is_first_move(board):
    return len(list_of_free_cells(board)) == 9


def is_board_completed(board):
    return len(list_of_free_cells(board)) == 0


def check_winner(board):
        
    WINNING_COMBINATIONS = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
]
    for combination in WINNING_COMBINATIONS:
        if all(board[cell] == board[combination[0]] != None for cell in combination):
            return board[combination[0]]


def machine_move(board):
    if is_first_move(board):
        board[5] = MACHINE
        return
    board[choice(list_of_free_cells(board))] = MACHINE


# ------------------------------ UI ------------------------------

ENTER_MOVE_INPUT = "Enter your move: "
INVALID_INPUT_MSG = "You must enter a number of a cell (1-9)."
INVALID_MOVE_MSG = "That cell is already taken."
YOU_WON = "You won!"
DRAW = "Draw!"
I_WON = "I won!"


def display_board(board: dict):
    def cell_display(cell):
        return board[cell] if is_taken_cell(board, cell) else cell

    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", cell_display(1), "  |  ", cell_display(2), "  |  ", cell_display(3), "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", cell_display(4), "  |  ", cell_display(5), "  |  ", cell_display(6), "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ", cell_display(7), "  |  ", cell_display(8), "  |  ", cell_display(9), "  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        cell_str = input(ENTER_MOVE_INPUT)
        try:
            cell = int(cell_str)
            if cell < 1 or cell > 9:
                print(INVALID_INPUT_MSG)
            elif is_taken_cell(board, cell):
                print(INVALID_MOVE_MSG)
            else:
                break
        except ValueError:
            print(INVALID_INPUT_MSG)
    board[int(cell)] = HUMAN


def main():
    board = {i: None for i in range(1, 10)}

    while True:
        machine_move(board)
        display_board(board)
        if check_winner(board) == MACHINE:
            print(I_WON)
            break
        if is_board_completed(board):  # Draw only posible after X's move (X always moves first)
            print(DRAW)
            break
        enter_move(board)
        display_board(board)
        if check_winner(board) == HUMAN:
            print(YOU_WON)
            break


if __name__ == "__main__":
    main()