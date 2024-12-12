from abc import ABC, abstractmethod
from game_messages import GameMessages
import random
from symbol import Symbol

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
        if board.is_first_move():
            return 5
        
        free_cells = board.get_free_cells()
        return random.choice(free_cells)

class MinimaxMachinePlayer(MachinePlayer):
    """Machine player using minimax algorithm for intelligent moves"""
    
    def _select_move(self, board):
        """Find the best move using minimax algorithm"""
        best_move, _ = self.minimax(board, True)
        return best_move

    def minimax(self, board, is_maximizing: bool):
        """Minimax algorithm to evaluate the best move"""
        winner = board.check_winner()
        if winner == self.symbol:
            return None, 1
        elif winner is not None:
            return None, -1
        elif board.is_board_full():
            return None, 0
        
        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None
        
        for cell in board.get_free_cells():
            original_value = board[cell]  # Store the original value
            board[cell] = self.symbol if is_maximizing else Symbol.HUMAN
            _, score = self.minimax(board, not is_maximizing)
            board[cell] = original_value  # Restore the original value
            
            if is_maximizing:
                if score > best_score:
                    best_score = score
                    best_move = cell
            else:
                if score < best_score:
                    best_score = score
                    best_move = cell
        
        return best_move, best_score