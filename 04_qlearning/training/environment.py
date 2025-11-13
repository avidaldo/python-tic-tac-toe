"""
Tic-Tac-Toe Environment for Q-Learning

This module provides the game environment for training and playing tic-tac-toe.
"""


class TicTacToeEnvironment:
    """
    Tic-Tac-Toe game environment.

    Handles board state, move validation, and win detection.
    """

    WINNING_COMBINATIONS = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]

    def __init__(self):
        """Initialize the environment with an empty board."""
        self.reset()

    def reset(self):
        """Reset the board for a new game."""
        self.board = {i: None for i in range(1, 10)}
        return self.board

    def get_available_actions(self):
        """
        Get list of available moves (empty cells).

        Returns:
            List of cell positions (1-9) that are empty
        """
        return [cell for cell, value in self.board.items() if value is None]

    def make_move(self, cell, symbol):
        """
        Place symbol in cell.

        Args:
            cell: Position 1-9
            symbol: 'X' or 'O'

        Returns:
            True if move was valid and made, False otherwise
        """
        if self.board.get(cell) is None:
            self.board[cell] = symbol
            return True
        return False

    def check_winner(self):
        """
        Check if there's a winner.

        Returns:
            'X', 'O', or None if no winner yet
        """
        for combo in self.WINNING_COMBINATIONS:
            cells = [self.board[pos] for pos in combo]
            if cells[0] is not None and cells[0] == cells[1] == cells[2]:
                return cells[0]
        return None

    def is_full(self):
        """
        Check if board is full (draw condition).

        Returns:
            True if all cells are occupied, False otherwise
        """
        return all(value is not None for value in self.board.values())

    def is_game_over(self):
        """
        Check if game ended.

        Returns:
            (is_over, result) where result is 'X', 'O', 'draw', or None
        """
        winner = self.check_winner()
        if winner:
            return True, winner
        elif self.is_full():
            return True, 'draw'
        else:
            return False, None

    def display(self):
        """Display the board in a nice format."""
        print("\n")
        for row in range(3):
            cells = []
            for col in range(3):
                cell_num = row * 3 + col + 1
                value = self.board[cell_num]
                cells.append(value if value else str(cell_num))
            print(" | ".join(cells))
            if row < 2:
                print("-" * 9)
        print("\n")
