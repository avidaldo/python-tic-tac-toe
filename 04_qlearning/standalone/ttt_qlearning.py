import os
from pathlib import Path

from ..training.environment import TicTacToeEnvironment
from ..training.q_learning_agent import QLearningAgent


class TicTacToe(TicTacToeEnvironment):
    """
    Interactive Tic-Tac-Toe game extending the base environment.

    Adds human interaction capabilities on top of the base environment.
    """

    def __init__(self, agent: QLearningAgent):
        """
        Initialize the game.

        Args:
            agent: The Q-learning agent to play against
        """
        super().__init__()
        self.agent = agent
        self.human_symbol = 'O'
        self.agent_symbol = agent.symbol

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('clear' if os.name == 'posix' else 'cls')

    def display_board(self):
        """Display the current board state in ASCII format with enhanced formatting."""
        print("\n")
        print("+-------+-------+-------+")
        for row in range(3):
            cells = []
            for col in range(3):
                cell_num = row * 3 + col + 1
                value = self.board[cell_num]
                if value is None:
                    cells.append(f"   {cell_num}   ")
                else:
                    cells.append(f"   {value}   ")
            print("|" + "|".join(cells) + "|")
            print("+-------+-------+-------+")
        print()

    def get_human_move(self):
        """Get and validate human player's move."""
        available = self.get_available_actions()

        while True:
            try:
                move = input(f"Enter your move (available: {available}): ")
                move = int(move)

                if move not in range(1, 10):
                    print(
                        "Invalid input! Please enter a number between 1 and 9."
                    )
                    continue

                if move not in available:
                    print("That cell is already taken! Choose another.")
                    continue

                return move

            except ValueError:
                print("Invalid input! Please enter a number.")
            except KeyboardInterrupt:
                print("\n\nGame interrupted by user.")
                exit(0)

    def get_agent_move(self):
        """Get the agent's move using its learned policy."""
        available = self.get_available_actions()
        move = self.agent.choose_action(self.board, available)
        return move

    def play_human_vs_agent(self, human_first: bool = True):
        """
        Play a game: human vs Q-learning agent.

        Args:
            human_first: If True, human goes first
        """
        self.clear_screen()
        print("=" * 50)
        print("   TIC-TAC-TOE: Human vs Q-Learning Agent")
        print("=" * 50)
        print(f"\nYou are: {self.human_symbol}")
        print(f"Agent is: {self.agent_symbol}")
        print("\nBoard positions:")
        print("  1 | 2 | 3")
        print("  ---------")
        print("  4 | 5 | 6")
        print("  ---------")
        print("  7 | 8 | 9")
        print()

        current_player = self.human_symbol if human_first else self.agent_symbol

        # Game loop
        while True:
            self.display_board()

            # Get move
            if current_player == self.human_symbol:
                print(f"Your turn ({self.human_symbol})")
                move = self.get_human_move()
            else:
                print(f"Agent's turn ({self.agent_symbol})")
                move = self.get_agent_move()
                print(f"Agent chose cell {move}")

            # Make move
            self.make_move(move, current_player)

            # Check game over
            is_over, result = self.is_game_over()
            if is_over:
                self.display_board()
                if result == 'draw':
                    print("Game Over - It's a draw!")
                elif result == self.human_symbol:
                    print("Congratulations! You won!")
                else:
                    print("Agent wins!")
                break

            # Switch player
            current_player = (self.agent_symbol if current_player
                              == self.human_symbol else self.human_symbol)



def main():
    """Main function to run the game."""
    print("=" * 50)
    print("   TIC-TAC-TOE: Q-Learning Agent")
    print("=" * 50)

    # Initialize agent
    agent = QLearningAgent(symbol='X', training_mode=False)

    # Load pre-trained Q-table from training directory
    q_table_file = Path(__file__).parent.parent / 'training' / 'q_table.pkl'

    if q_table_file.exists():
        agent.load(str(q_table_file))
        stats = agent.get_stats()
        print(f"\nAgent statistics:")
        print(f"  - Learned states: {stats['unique_states']}")
        print(f"  - Total Q-values: {stats['total_entries']}")
        print(f"  - Avg Q-value: {stats['avg_q_value']:.3f}")
    else:
        print(f"\nWarning: No trained Q-table found at '{q_table_file}'")
        print("The agent will play randomly. Please train the agent first.")
        print("Run: python3 -m 04_qlearning.training.train_qlearning")
        response = input("\nContinue anyway? (y/n): ")
        if response.lower() != 'y':
            return

    # Game menu
    while True:
        print("\n" + "=" * 50)
        print("Options:")
        print("  1. Play (Human first)")
        print("  2. Play (Agent first)")
        print("  3. View agent statistics")
        print("  4. Quit")
        print("=" * 50)

        choice = input("\nEnter choice: ")

        if choice == '1':
            game = TicTacToe(agent)
            game.play_human_vs_agent(human_first=True)
        elif choice == '2':
            game = TicTacToe(agent)
            game.play_human_vs_agent(human_first=False)
        elif choice == '3':
            stats = agent.get_stats()
            print("\n" + "=" * 50)
            print("Agent Statistics:")
            print("=" * 50)
            print(f"Total Q-table entries: {stats['total_entries']}")
            print(f"Unique states learned: {stats['unique_states']}")
            print(f"Average Q-value: {stats['avg_q_value']:.3f}")
            print(f"Max Q-value: {stats['max_q_value']:.3f}")
            print(f"Min Q-value: {stats['min_q_value']:.3f}")
        elif choice == '4':
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
