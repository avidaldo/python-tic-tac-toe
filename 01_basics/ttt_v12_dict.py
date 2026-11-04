"""
The game board is defined as a dictionary where each key identifies the number
that will be shown to identify the cell. The values of each key are None when
there is no piece and the constants MACHINE and HUMAN when there is a machine
or human piece respectively.
"""

from random import choice

MACHINE = "X"
HUMAN = "O"



# ------------------------------ UI ------------------------------
ENTER_MOVE_INPUT = "Introduce el número de una casilla libre (1-9): "
INVALID_INPUT_MSG = "Entrada no válida. Introduce un número del 1 al 9."
INVALID_MOVE_MSG = "Esa casilla ya está ocupada. Elige otra."

I_WON = "¡La máquina ha ganado!"
YOU_WON = "¡Has ganado!"
DRAW = "¡Empate!"


# ------------------------------ Logic ------------------------------


# Listado de celdas libres en el tablero. 
# Se utiliza una lista por comprensión para recorrer los números del 1 al 9.
def list_of_free_cells(board):
    return [i for i in range(1, 10) if board[i] is None]




def check_winner(board):
        
    WINNING_COMBINATIONS = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
]
    for combination in WINNING_COMBINATIONS:
        if all(board[cell] == board[combination[0]] != None for cell in combination):
        # Comprueba si todas las celdas en la combinación ganadora tienen el mismo valor (ya sea "X" o "O") y no son None. 
        # Si es así, significa que hay un ganador.
            return board[combination[0]]



# Comprueba la longitud de la lista de celdas libres. Si es 0, significa que el tablero está completo.
def is_board_completed(board):
    return len(list_of_free_cells(board)) == 0


# Función que realiza el movimiento de la máquina. Selecciona una celda libre al azar y coloca la pieza de la máquina ("X").
def machine_move(board):  
    board[choice(list_of_free_cells(board))] = MACHINE
    


# función definida dentro de otra función, también llamada función anidada (nested function)
def display_board(board: dict):
    def cell_display(cell):
        return board[cell] if board[cell] is not None else cell

# Este print está dentro de la función display_board, por lo que se ejecutará cada vez que se llame a display_board.
# cell_display se llama para cada celda del tablero (del 1 al 9) y devuelve el contenido de la celda o el número de la celda si está libre.

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




def human_move(board):
    while True:
        # Solicita al usuario que ingrese su movimiento. Se guarda como string en cell_str.
        cell_str = input(ENTER_MOVE_INPUT)
        try:
            # Convierte el string ingresado por el usuario a un entero. 
            cell = int(cell_str)
            # Comprueba la valided del movimiento.
            if cell < 1 or cell > 9:
                print(INVALID_INPUT_MSG)
            elif board[cell] is not None:  # if is_taken_cell(board, cell):
                print(INVALID_MOVE_MSG)
            else:
                # Si el movimiento es válido, se sale del bucle while.
                break
        except ValueError:
            print(INVALID_INPUT_MSG)
    board[int(cell)] = HUMAN


def main():
    # Crea un tablero vacío representado como un diccionario con claves del 1 al 9 y valores None.
    board = {i: None for i in range(1, 10)}

    # Mostramos el tablero vacío.
    display_board(board)

    current_player = choice([HUMAN, MACHINE])

    print("¡Comienza la partida!")
    print("Empiezas tú." if current_player == HUMAN else "Empieza la máquina.")

    while True:
        if current_player == MACHINE:
            machine_move(board)
        else:
            human_move(board)
        display_board(board)

        # Comprobamos si el jugador actual ha ganado.
        winner = check_winner(board)

        if winner == MACHINE:
            print(I_WON)
            break

        if winner == HUMAN:
            print(YOU_WON)
            break

        # Comprobamos si el tablero está completo.
        if is_board_completed(board):
            print(DRAW)
            break
        # Cambiamos de jugador.
        current_player = HUMAN if current_player == MACHINE else MACHINE



if __name__ == "__main__":
    main()