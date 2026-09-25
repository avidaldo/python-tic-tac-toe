import random
from .agent import Agent


class RandomAgent(Agent):
    """
    A simple agent that chooses random available actions.
    Useful as a baseline opponent.
    """

    def __init__(self, symbol: str = 'O') -> None:
        super().__init__(symbol)

    def choose_action(self, board: dict[int, str | None], available_actions: list[int] | None = None) -> int:
        if available_actions is None:
            available_actions = [k for k, v in board.items() if v is None]
        return random.choice(available_actions)
