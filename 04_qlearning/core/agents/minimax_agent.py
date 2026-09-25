"""
Minimax Agent for Tic-Tac-Toe

This module implements a perfect Tic-Tac-Toe player using the Minimax algorithm.
"""

import math
import random
from .agent import Agent

class MinimaxAgent(Agent):
    """
    A Tic-Tac-Toe agent that plays optimally using the Minimax algorithm.
    It will never lose, only win or draw.
    """
    
    def __init__(self, symbol: str = 'O') -> None:
        """
        Initialize the Minimax agent.
        
        Args:
            symbol: The player's symbol ('X' or 'O')
        """
        super().__init__(symbol)
        self.opponent_symbol = 'X' if symbol == 'O' else 'O'
        self.cache: dict[tuple[tuple[str | None, ...], bool], int | float] = {}
        
    def choose_action(self, board: dict[int, str | None], available_actions: list[int] | None = None) -> int:
        """
        Choose the optimal action for the current board state.
        
        Args:
            board: Current board dictionary {1..9: 'X'/'O'/None}
            available_actions: Optional list of available moves (calculated if None)
            
        Returns:
            Best move (1-9)
        """
        # Optimization: If it's the first move and center is open, take it.
        # This saves computation time for the most expensive first step.
        if sorted(list(board.keys())) == list(range(1, 10)) and all(v is None for v in board.values()):
            return 5
            
        # If the opponent opened in the center, a corner is an optimal reply
        if len([v for v in board.values() if v is not None]) == 1 and board[5] is not None:
            return random.choice([1, 3, 7, 9])

        if available_actions is None:
            available_actions = [k for k, v in board.items() if v is None]
            
        # Cached values are relative to the depth of the search root, so each move starts a fresh cache
        self.cache = {}

        move_scores: dict[int, int | float] = {}
        for move in available_actions:
            board[move] = self.symbol
            move_scores[move] = self.minimax(board, 0, False)
            board[move] = None

        # Several moves can be equally optimal; picking one at random makes the games more varied
        best_score = max(move_scores.values())
        return random.choice([move for move, score in move_scores.items() if score == best_score])

    def get_board_tuple(self, board: dict[int, str | None]) -> tuple[str | None, ...]:
        return tuple(board[i] for i in range(1, 10))

    def minimax(self, board: dict[int, str | None], depth: int, is_maximizing: bool) -> int | float:
        """
        Recursive Minimax function to evaluate board states.
        
        Args:
            board: Current board state
            depth: Current depth in game tree
            is_maximizing: True if it's the agent's turn, False for opponent
            
        Returns:
            Score (-10 for loss, 0 for draw, +10 for win)
        """
        board_tuple = self.get_board_tuple(board)
        state_key = (board_tuple, is_maximizing)
        
        if state_key in self.cache:
            return self.cache[state_key]

        score = self.evaluate(board)
        
        # If terminal state, return score
        if score == 10:
            return score - depth  # Prefer faster wins
        if score == -10:
            return score + depth  # Prefer slower losses
        if not any(v is None for v in board.values()):
            return 0  # Draw
            
        if is_maximizing:
            best = -math.inf
            for i in range(1, 10):
                if board[i] is None:
                    board[i] = self.symbol
                    best = max(best, self.minimax(board, depth + 1, False))
                    board[i] = None
            self.cache[state_key] = best
            return best
        else:
            best = math.inf
            for i in range(1, 10):
                if board[i] is None:
                    board[i] = self.opponent_symbol
                    best = min(best, self.minimax(board, depth + 1, True))
                    board[i] = None
            self.cache[state_key] = best
            return best

    def evaluate(self, board: dict[int, str | None]) -> int:
        """
        Evaluate the board state.
        
        Returns:
            +10 if agent wins
            -10 if opponent wins
            0 otherwise
        """
        # Check rows
        for i in range(1, 8, 3):
            if board[i] == board[i+1] == board[i+2]:
                if board[i] == self.symbol: return 10
                if board[i] == self.opponent_symbol: return -10
                
        # Check columns
        for i in range(1, 4):
            if board[i] == board[i+3] == board[i+6]:
                if board[i] == self.symbol: return 10
                if board[i] == self.opponent_symbol: return -10
                
        # Check diagonals
        if board[1] == board[5] == board[9]:
            if board[1] == self.symbol: return 10
            if board[1] == self.opponent_symbol: return -10
            
        if board[3] == board[5] == board[7]:
            if board[3] == self.symbol: return 10
            if board[3] == self.opponent_symbol: return -10
            
        return 0
