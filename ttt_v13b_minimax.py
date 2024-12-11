"""
Versión que implementa el algoritmo Minimax para la lógica de la máquina. No puede perder.
Además, permite elegir quién empieza la partida.

Programación recursiva en python: https://www.youtube.com/watch?v=cgg1ACU49aQ
Minimax en el tres en raya: https://www.youtube.com/watch?v=SLgZhpDsrfc

Variantes de esta implementación:
- Usar la profundidad del árbol de juego para priorizar ganar en menos movimientos.
- Usar alfa-beta pruning para reducir el número de nodos evaluados.
"""

from random import choice

AI = "X"
HUMAN = "O"

    
def minimax(board, is_maximizing) -> tuple:
    
    # Terminal states
    if check_winner(board) == AI:
        return 1, None # AI wins -> increase score (maximize)
    if check_winner(board) == HUMAN:
        return -1, None # Human wins -> decrease score (minimize)
    if is_board_completed(board):
        return 0, None # Draw -> neutral score

    # Recursive states
    if is_maximizing: # AI's turn
        best_score = float("-inf") # Initialize best score as the worst possible
        best_move = None # Initialize best move as None
        for cell in list_of_free_cells(board): # For each possible move
            board[cell] = AI # Make the move, opening a new branch
            score, _ = minimax(board, False) # Evaluate the move
            board[cell] = None # Leave the cell as it was after evaluating that branch
            if score > best_score: # If the score of that branch is better than previous best score
                best_score = score # Keep the best score of that branch
                best_move = cell # Keep the best move
        return best_score, best_move
    else: # Human's turn (minimizing)
        best_score = float("inf")
        best_move = None
        for cell in list_of_free_cells(board):
            board[cell] = HUMAN # Human makes a move
            score, _ = minimax(board, True)
            board[cell] = None
            if score < best_score: # Human tries to minimize the score
                best_score = score
                best_move = cell
        return best_score, best_move
    


def minimax_move(board): # AI makes a move using minimax
    _, best_move = minimax(board, True)
    return best_move



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


def random_move(board):
    return board[choice(list_of_free_cells(board))]


def machine_move(board, level="minimax"):
    board[random_move(board) if level == "random" else minimax_move(board)] = AI


# ------------------------------ UI ------------------------------


WHO_STARTS = "Do you want to start? (y/n): "
ENTER_MOVE_INPUT = "Enter your move: "
INVALID_INPUT_MSG = "You must enter a number of a cell (1-9)."
INVALID_MOVE_MSG = "That cell is already taken."
YOU_WON = "You won!"
DRAW = "Draw!"
I_WON = "I won!"
COMPUTER_THINKING = "Computer is thinking..."


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
    

def human_starts():
    return input(WHO_STARTS).lower() == "y"


def main():
    board = {i: None for i in range(1, 10)}
    turn = HUMAN if human_starts() else AI

    display_board(board)
    while True:
        if turn == AI:
            print(COMPUTER_THINKING)
            machine_move(board)
        else:
            enter_move(board)
            
        display_board(board)
        
        if check_winner(board) == turn:
            print(YOU_WON if turn == HUMAN else I_WON)
            break
            
        if is_board_completed(board):
            print(DRAW)
            break
            
        turn = HUMAN if turn == AI else AI
        
        


if __name__ == "__main__":
    main()