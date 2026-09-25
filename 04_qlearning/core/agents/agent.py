"""
Abstract base class for Tic-Tac-Toe agents.
"""

from abc import ABC, abstractmethod


class Agent(ABC):
    """
    Base class for every Tic-Tac-Toe agent.
    
    Subclasses MUST implement `choose_action`.
    """

    def __init__(self, symbol: str) -> None:
        """
        Args:
            symbol: The player's symbol ('X' or 'O').
        """
        self.symbol = symbol

    @abstractmethod
    def choose_action(self, board: dict[int, str | None], available_actions: list[int]) -> int:
        """
        Choose an action for the current board state.

        Args:
            board: Current board {1..9: 'X'/'O'/None}
            available_actions: List of empty cell positions (1-9)

        Returns:
            Chosen move (1-9)
        """
        ...
