import random
from abc import ABC, abstractmethod
from enum import Enum

class GameMessages:
    ENTER_MOVE = "Enter your move (1-9): "
    INVALID_NUMBER = "You must enter a number between 1 and 9."
    CELL_TAKEN = "That cell is already taken."
    INVALID_INPUT = "Invalid input. Please enter a number."
    
    HUMAN_WIN = "Congratulations! You won!"
    MACHINE_WIN = "I won! Better luck next time."
    DRAW = "It's a draw!"
    
    DIFFICULTY_PROMPT = (
        "Select difficulty level:\n"
        "1. Easy (Random moves)\n"
        "2. Hard (Minimax algorithm)\n"
        "Choose 1/(2): "
    )
    
    FIRST_PLAYER_PROMPT = (
        "Who wants to start?\n"
        "1. Human\n"
        "2. Machine\n"
        "Choose 1/(2): "
    )
    
    
class Symbol(Enum):
    HUMAN = 'O'
    AI = 'X'

    def __str__(self):
        return self.value


class Player(ABC):
    """Abstract base class for players"""
    def __init__(self, symbol):
        self.symbol = symbol
    
    @abstractmethod
    def make_move(self, board):
        """Abstract method for making a move; any subclass must implement this"""
        pass


class HumanPlayer(Player):
    """Human player with input-based move selection"""
    def make_move(self, board):
        """Prompt user for a valid move"""
        while True:
            try:
                cell_str = input(GameMessages.ENTER_MOVE)
                cell = int(cell_str)
                
                if not 1 <= cell <= 9:
                    print(GameMessages.INVALID_NUMBER)
                    continue
                
                if board.is_cell_taken(cell):
                    print(GameMessages.CELL_TAKEN)
                    continue
                
                board[cell] = self.symbol
                break
            
            except ValueError:
                print(GameMessages.INVALID_INPUT)


class MachinePlayer(Player):
    """Base class for machine players with a common interface"""
    def __init__(self, symbol):
        super().__init__(symbol)

    @abstractmethod
    def _select_move(self, board):
        """Abstract method to select a move strategy"""
        pass

    def make_move(self, board):
        """Standard move-making process for machine players"""
        move = self._select_move(board)
        board[move] = self.symbol


class RandomMachinePlayer(MachinePlayer):
    """Machine player using random move selection"""
    def _select_move(self, board):
        """Simple random move strategy"""
        # Special case for first move: always take center if possible
        if board.is_first_move():
            return 5
        
        # Select a random free cell
        free_cells = board.get_free_cells()
        return random.choice(free_cells)


class MinimaxMachinePlayer(MachinePlayer):
    """Machine player using minimax algorithm for intelligent moves"""
    def _select_move(self, board):
        """Find the best move using minimax algorithm"""
        def minimax(board, is_maximizing):
            # Base cases for recursion
            winner = board.check_winner()
            if winner == self.symbol:
                return 1
            elif winner is not None:
                return -1
            elif board.is_board_full():
                return 0
            
            # Recursive minimax logic
            if is_maximizing:
                best_score = float('-inf')
                for cell in board.get_free_cells():
                    board[cell] = self.symbol
                    score = minimax(board, False)
                    board[cell] = None  # Undo move
                    best_score = max(best_score, score)
                return best_score
            else:
                best_score = float('inf')
                opponent_symbol = Symbol.HUMAN if self.symbol == Symbol.AI else Symbol.AI
                for cell in board.get_free_cells():
                    board[cell] = opponent_symbol
                    score = minimax(board, True)
                    board[cell] = None  # Undo move
                    best_score = min(best_score, score)
                return best_score
        
        # Find the best move
        best_move = None
        best_score = float('-inf')
        for cell in board.get_free_cells():
            board[cell] = self.symbol
            score = minimax(board, False)
            board[cell] = None  # Undo move
            
            if score > best_score:
                best_score = score
                best_move = cell
        
        return best_move

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
        

class TicTacToeGame:
    """Manages the overall game flow"""
    def __init__(self):
        self.board = GameBoard()
        
    def promt_select_difficulty(self):
        while True:
            try:
                difficulty = input(GameMessages.DIFFICULTY_PROMPT)
                if difficulty == '1':
                    return RandomMachinePlayer
                else:
                    return MinimaxMachinePlayer
            except ValueError:
                print(GameMessages.INVALID_INPUT)

    def promt_select_first_player(self):
        while True:
            try:
                first_player = input(GameMessages.FIRST_PLAYER_PROMPT)
                if first_player == '1':
                    return Symbol.HUMAN
                else:
                    return Symbol.AI
            except ValueError:
                print(GameMessages.INVALID_INPUT)

    def play(self):
        """
        Main game loop
        """
        machine_player = self.promt_select_difficulty()
        current_symbol = self.promt_select_first_player()
        
        players = { # Configure players dictionary
            Symbol.HUMAN: HumanPlayer(Symbol.HUMAN),
            Symbol.AI: machine_player(Symbol.AI)
        }
        
        print(self.board)
        # Game loop
        while True:
            current_player = players[current_symbol] # Get current player based on symbol
            current_player.make_move(self.board) # Current player makes a move
            print(self.board)

            # Check for win or draw
            winner = self.board.check_winner()
            if winner:
                if winner == Symbol.AI:
                    print(GameMessages.MACHINE_WIN)
                else:
                    print(GameMessages.HUMAN_WIN)
                break

            if self.board.is_board_full():
                print(GameMessages.DRAW)
                break

            # Switch turns
            current_symbol = Symbol.AI if current_symbol == Symbol.HUMAN else Symbol.HUMAN


def main():
    """Entry point for the Tic-Tac-Toe game"""
    game = TicTacToeGame()
    game.play()


if __name__ == "__main__":
    main()