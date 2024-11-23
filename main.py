from __future__ import annotations  # Let's postpone the type evaluation because Python can't handle that yet.
from typing import Callable, List, Dict, Optional
from random import choice

# ------------------------------- Configuración -------------------------------

# X, Y. Seriously, it's 3x3. It's not like we’re trying to build the next Google here.
X, Y = 3,3   # Dimensions of the board. A "tiny" tic-tac-toe grid. Nothing fancy.
# Na just adjust to your preferences

# We define the players as characters, because humans can't play without understanding ASCII art.
MACHINE, HUMAN = "X", "O"  # Machine plays as X, Human as O. We're keeping it old school, no need for anything complicated here.

# The messages are for emotional feedback. Because, you know, gaming is all about feelings.
DRAW_TEXT, YOU_WON_TEXT, I_WON_TEXT = "Draw!", "You won!", "I won!"  # Congratulations or frustration, take your pick.

INVALID_MOVE_TEXT = "Invalid move. Try again."  # Someone didn't play by the rules. Shocking.

# -------------------------------- Funciones ----------------------------------

# Let's start by creating the board. It's a dictionary, because arrays are for amateurs.
create_board: Callable[[int, int], Dict[int, Optional[str]]] = lambda x, y: {
    i: None for i in range(1, x * y + 1)  # A dictionary where each cell is a key and the value is None, like a blank canvas.
    # If you don't know what a dictionary is... well, read a book. Or check Google, I don't care.
}

# Generate all winning combinations dynamically. This is where things get a little too "mathy" for your average player.
winning_combinations: Callable[[int, int], List[List[int]]] = lambda x, y: (
        [[row * x + col + 1 for col in range(x)] for row in range(y)] +  # Rows. Simple enough, right? Just adding them up.
        [[col + row * y + 1 for row in range(y)] for col in range(x)] +  # Columns. Because, you know, the grid isn't one-dimensional.
        [[i * (x + 1) + 1 for i in range(min(x, y))]] +  # Main diagonal. It's all about that 45-degree angle, baby.
        [[(i + 1) * (x - 1) + 1 for i in range(min(x, y))]]  # Anti-diagonal. Opposite of the main diagonal. Who thought of this? Genius.
)

# Here, we display the board. It's just a print statement, but you need to *feel* the layout.
display_board: Callable[[Dict[int, Optional[str]]], None] = lambda board: print(
    "\n".join(
        ["+".join(["------"] * X)] +  # A neat little separator, because why not add some style to this hellhole.
        [
            "| " + " | ".join(
                f"  {board.get(row * X + col + 1, row * X + col + 1) or (row * X + col + 1)}  "
                # If the cell is filled, show that. If it's empty, display the number of the cell. Genius, right?
                for col in range(X)
            ) + " |"
            for row in range(Y)
        ] +
        ["+".join(["------"] * X)]
    )
)

# Check if a player has won. Simple brute force check, because who needs optimizations for a 3x3 grid?
victory_for: Callable[[Dict[int, Optional[str]], str], bool] = lambda board, sign: any(
    all(board.get(cell) == sign for cell in combo) for combo in winning_combinations(X, Y)
    # This is your typical "look through the list of winning combos and check if the player has filled it". No magic here, just logic.
)

# Check if the board is full. Because, honestly, if it's full, we have a game over situation.
is_board_full: Callable[[Dict[int, Optional[str]]], bool] = lambda board: all(
    value is not None for value in board.values()
    # If any of the cells are still None, the board is not full. If all cells are filled... well, it’s over.
)

# Change turns. No rocket science here. The human goes, then the machine, then the human, etc.
next_turn: Callable[[str], str] = lambda current: MACHINE if current == HUMAN else HUMAN
# Yeah, I know. It's just a conditional. But you could have used a dictionary for this too. Get over it.

# Update the board. We update it immutably because we’re not savages here.
update_board: Callable[[Dict[int, Optional[str]], int, str], Dict[int, Optional[str]]] = lambda board, cell, sign: (
    board if board[cell] is not None else {**board, cell: sign}
    # Here, we’re copying the board and updating the cell. "Immutability", you might have heard of it.
)

# Player move function. Get ready for infinite recursion... until the player makes a valid move, that is.
def player_move(board: Dict[int, Optional[str]]) -> int:
    while True:
        try:
            cell = int(input(f"Enter the cell number (1-{X * Y}): "))
            if cell < 1 or cell > X * Y:  # Making sure it’s in bounds. Of course.
                print(INVALID_MOVE_TEXT)  # If the move is out of bounds, it’s invalid. Shocking... isn't?
            elif board[cell] is not None:  # If the cell is taken, it’s invalid. Common sense.
                print(INVALID_MOVE_TEXT)
            else:
                return cell  # Finally mate...
        except (ValueError, KeyError):  # This catches anything that isn’t a number. Human error at its finest.
            print(INVALID_MOVE_TEXT)

# Machine move function. Picking a random cell from the available ones because, why not.
machine_move: Callable[[Dict[int, Optional[str]]], int] = lambda board: choice(
    [cell for cell, value in board.items() if value is None]
    # The machine is not playing chess. It’s just picking an available spot randomly. No strategy, just brute force.
)

# -------------------------------- Main --------------------------------------

# Main function. The heart of the game. Where everything comes together in this beautiful disaster.
def main() -> None:
    board = create_board(X, Y)  # Create the board. Seriously, don’t overthink it. It’s just a dictionary.
    turn = HUMAN  # Start with the human. Because they’re supposed to be better at this, right?

    while True:
        print(f"\n{'TURNO JUGADOR' if turn == HUMAN else 'TURNO IA'}")  # Print who’s turn it is. Because we like to be dramatic.

        display_board(board)

        # Get the move based on whose turn it is. Player or machine? It’s a very hard decision to make...
        move = (
            player_move(board) if turn == HUMAN
            else machine_move(board)  # If it’s the machine’s turn, it picks randomly. What else would it do?
        )

        # Update the board with the new move.
        new_board = update_board(board, move, turn)

        # Check if the current player has won. It's simple logic, really.
        if victory_for(new_board, turn):
            display_board(new_board)
            print(YOU_WON_TEXT if turn == HUMAN else I_WON_TEXT)
            break

        # Check if the board is full, aka the game ends in a draw. We don’t want to continue a pointless game.
        if is_board_full(new_board):
            display_board(new_board)
            print(DRAW_TEXT)
            break

        # Switch turns. Because games are about fairness, I guess.
        board, turn = new_board, next_turn(turn)


if __name__ == "__main__":
    main()
