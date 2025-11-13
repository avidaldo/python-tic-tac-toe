"""
Q-Learning Machine Player for OOP Tic-Tac-Toe

This module provides a QLearningMachinePlayer class that integrates
the trained Q-learning agent into the object-oriented tic-tac-toe game.
"""

from pathlib import Path

from ..training.q_learning_agent import QLearningAgent


class QLearningMachinePlayer:
    """
    Machine player using a trained Q-learning agent.

    This class wraps the QLearningAgent to work with the OOP game structure.
    It follows the same interface as other players (HumanPlayer, RandomMachinePlayer,
    MinimaxMachinePlayer) from the 03_oop version.
    """

    def __init__(self, symbol, q_table_path=None):
        """
        Initialize Q-learning player.

        Args:
            symbol: Player symbol ('X' or 'O')
            q_table_path: Path to trained Q-table file (optional)
        """
        self.symbol = symbol

        # Create Q-learning agent in play mode (no training, no exploration)
        self.agent = QLearningAgent(
            symbol=symbol,
            training_mode=False,
            epsilon=0.0
        )

        # Load Q-table if provided
        if q_table_path:
            self.load_q_table(q_table_path)
        else:
            # Try to load default Q-table
            default_path = Path(__file__).parent.parent / 'training' / 'q_table.pkl'
            if default_path.exists():
                self.load_q_table(str(default_path))
            else:
                print("Warning: No Q-table loaded. Agent will play randomly.")

    def load_q_table(self, path):
        """Load Q-table from file."""
        try:
            self.agent.load(path)
            print(f"Q-learning agent loaded successfully")
        except Exception as e:
            print(f"Error loading Q-table: {e}")

    def _select_move(self, board):
        """
        Select move using Q-learning agent.

        Args:
            board: GameBoard object

        Returns:
            Selected cell position (1-9)
        """
        # Convert GameBoard to dict format expected by agent
        board_dict = {}
        for i in range(1, 10):
            cell_value = board[i]
            # Convert Symbol enum to string if needed
            if cell_value is not None:
                board_dict[i] = str(cell_value) if hasattr(cell_value, 'value') else cell_value
            else:
                board_dict[i] = None

        # Get available moves
        available = board.get_free_cells()

        # Agent chooses action
        move = self.agent.choose_action(board_dict, available)

        return move

    def make_move(self, board):
        """
        Make a move on the board.

        Args:
            board: GameBoard object
        """
        move = self._select_move(board)
        board[move] = self.symbol
        return move
