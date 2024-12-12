class GameBoard:
    """
    Manages the state and rules of the Tic-Tac-Toe board.
    """
    def __init__(self):
        """Initialize an empty game board."""
        self._board = {i: None for i in range(1, 10)}
        self._WINNING_COMBINATIONS = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
            (1, 5, 9), (3, 5, 7)              # Diagonals
        ]
        
    def __getitem__(self, cell) -> str:
        return self._board[cell]
    
    def __setitem__(self, cell, symbol):
        self._board[cell] = symbol

    def is_cell_taken(self, cell) -> bool:
        return self[cell] is not None

    def get_free_cells(self) -> list:
        return [i for i in range(1, 10) if not self.is_cell_taken(i)]

    def is_first_move(self) -> bool:
        return len(self.get_free_cells()) == 9

    def is_board_full(self) -> bool:
        return len(self.get_free_cells()) == 0

    def check_winner(self):
        """
        Determine if there's a winner and return the winning symbol.
        
        Returns:
            str or None: Winning player's symbol, or None if no winner
        """
        for combination in self._WINNING_COMBINATIONS:
            if all(self._board[cell] == self._board[combination[0]] != None 
                   for cell in combination):
                return self._board[combination[0]]
        return None

    def __str__(self):
        """Return a string representation of the current board state."""
        def cell_display(cell):
            return self._board[cell] if self.is_cell_taken(cell) else cell
        board_str = "+-------+-------+-------+\n"
        board_str += "|       |       |       |\n"
        board_str += f"|   {cell_display(1)}   |   {cell_display(2)}   |   {cell_display(3)}   |\n"
        board_str += "|       |       |       |\n"
        board_str += "+-------+-------+-------+\n"
        board_str += "|       |       |       |\n"
        board_str += f"|   {cell_display(4)}   |   {cell_display(5)}   |   {cell_display(6)}   |\n"
        board_str += "|       |       |       |\n"
        board_str += "+-------+-------+-------+\n"
        board_str += "|       |       |       |\n"
        board_str += f"|   {cell_display(7)}   |   {cell_display(8)}   |   {cell_display(9)}   |\n"
        board_str += "|       |       |       |\n"
        board_str += "+-------+-------+-------+"
        return board_str