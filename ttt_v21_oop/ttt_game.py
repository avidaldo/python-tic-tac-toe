from game_board import GameBoard
from player import HumanPlayer, RandomMachinePlayer, MinimaxMachinePlayer
from game_messages import GameMessages
from symbol import Symbol


class TicTacToeGame:
    """Manages the overall game flow"""

    RANDOM = '1'
    MINIMAX = '2'
    
    FIRST_PLAYER_HUMAN = '1'
    FIRST_PLAYER_AI = '2'
                
    def __init__(self):
        self.board = GameBoard()
        
    def prompt_select_difficulty(self):
        while True:
            try:
                difficulty = input(GameMessages.DIFFICULTY_PROMPT)
                if difficulty == self.RANDOM:
                    return RandomMachinePlayer
                else: # default to Minimax
                    return MinimaxMachinePlayer
            except ValueError:
                print(GameMessages.INVALID_INPUT)

    def prompt_select_first_player(self):
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
        """
        Main game loop
        """
        machine_player = self.prompt_select_difficulty()
        current_symbol = self.prompt_select_first_player()
        
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