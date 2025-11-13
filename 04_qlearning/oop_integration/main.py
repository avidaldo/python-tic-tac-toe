"""
Tic-Tac-Toe OOP Game with Q-Learning Agent

This version uses a trained Q-learning agent as the AI opponent.
"""

import sys
from pathlib import Path

# Add path for importing from 03_oop (external dependency)
sys.path.insert(0, str(Path(__file__).parent.parent.parent / '03_oop'))

from game_board import GameBoard
from player import HumanPlayer
from game_messages import GameMessages
from symbol import Symbol
from .q_learning_player import QLearningMachinePlayer


class TicTacToeGame:
    """Manages the overall game flow with Q-Learning agent"""

    FIRST_PLAYER_HUMAN = '1'
    FIRST_PLAYER_AI = '2'

    def __init__(self):
        self.board = GameBoard()


    def prompt_select_first_player(self):
        """Prompt user to select who goes first"""
        while True:
            try:
                first_player = input(GameMessages.FIRST_PLAYER_PROMPT)
                if first_player == self.FIRST_PLAYER_HUMAN:
                    return Symbol.HUMAN
                else: # default to AI
                    return Symbol.AI
            except ValueError:
                print(GameMessages.INVALID_INPUT)

    def play(self):
        """Main game loop"""
        current_symbol = self.prompt_select_first_player()

        # Configure players dictionary with Q-Learning agent
        players = {
            Symbol.HUMAN: HumanPlayer(Symbol.HUMAN),
            Symbol.AI: QLearningMachinePlayer(Symbol.AI)
        }

        print(self.board)

        # Game loop
        while True:
            current_player = players[current_symbol]
            current_player.make_move(self.board)
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
    """Entry point for the game"""
    print("=" * 60)
    print("  TIC-TAC-TOE with Q-Learning")
    print("=" * 60)
    game = TicTacToeGame()
    game.play()


if __name__ == "__main__":
    main()
