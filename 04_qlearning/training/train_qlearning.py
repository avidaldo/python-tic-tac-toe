"""
Training Script for Q-Learning Tic-Tac-Toe Agent

This script trains a Q-learning agent to play tic-tac-toe by having it
play many games against different opponents (random and self-play).
"""

import random
from pathlib import Path

# Support both direct execution and package imports
try:
    from .q_learning_agent import QLearningAgent
    from .environment import TicTacToeEnvironment
except ImportError:
    from q_learning_agent import QLearningAgent
    from environment import TicTacToeEnvironment


def play_training_game(agent, opponent_type='random', agent_first=True, opponent_agent=None):
    """
    Play one training game.

    Args:
        agent: The Q-learning agent to train
        opponent_type: 'random' or 'self' (self-play)
        agent_first: If True, agent goes first
        opponent_agent: Another agent for self-play (optional)

    Returns:
        Result: 'win', 'loss', or 'draw' from agent's perspective
    """
    env = TicTacToeEnvironment()
    agent.reset_episode()

    agent_symbol = agent.symbol
    opponent_symbol = 'O' if agent_symbol == 'X' else 'X'

    current_player = agent_symbol if agent_first else opponent_symbol

    # Game loop
    while True:
        available = env.get_available_actions()

        # Get move
        if current_player == agent_symbol:
            # Agent's turn
            move = agent.choose_action(env.board, available)
        else:
            # Opponent's turn
            if opponent_type == 'random':
                move = random.choice(available)
            elif opponent_type == 'self' and opponent_agent:
                move = opponent_agent.choose_action(env.board, available)
            else:
                move = random.choice(available)

        # Make move
        env.make_move(move, current_player)
        is_over, result = env.is_game_over()

        if current_player == agent_symbol:
            # Agent just moved - time to learn!
            if is_over:
                # Game ended - learn with final reward and next_board=None
                if result == agent_symbol:
                    reward = 1.0  # WIN!
                elif result == opponent_symbol:
                    reward = -1.0  # LOSS!
                else:
                    reward = 0.0  # DRAW

                # Learn with next_board=None to indicate terminal state
                agent.learn(reward=reward, next_board=None)
                agent.reset_episode()  # Clear history for next game

                return 'win' if result == agent_symbol else (
                    'loss' if result == opponent_symbol else 'draw')
            else:
                # Game continues - small penalty for each move
                agent.learn(reward=-0.01, next_board=env.board)
        elif is_over:
            # Opponent's move ended the game
            agent.reset_episode()  # Clear history for next game
            return 'loss' if result == opponent_symbol else 'draw'

        # Switch player
        current_player = opponent_symbol if current_player == agent_symbol else agent_symbol


def train_agent(n_episodes=50000, learning_rate=0.1, discount_factor=0.9,
                epsilon_start=1.0, epsilon_end=0.01, epsilon_decay=0.9995,
                eval_every=5000, save_file="q_table.pkl"):
    """
    Train a Q-learning agent.

    Args:
        n_episodes: Number of training episodes
        learning_rate: Learning rate (α)
        discount_factor: Discount factor (γ)
        epsilon_start: Initial exploration rate
        epsilon_end: Minimum exploration rate
        epsilon_decay: Exponential decay rate for epsilon
        eval_every: Evaluate every N episodes
        save_file: File to save Q-table
    """
    print("=" * 60)
    print("  Training Q-Learning Agent for Tic-Tac-Toe")
    print("=" * 60)
    print(f"\nTraining parameters:")
    print(f"  Episodes: {n_episodes}")
    print(f"  Learning rate (α): {learning_rate}")
    print(f"  Discount factor (γ): {discount_factor}")
    print(
        f"  Epsilon: {epsilon_start} → {epsilon_end} (decay: {epsilon_decay})")
    print()

    # Create agent
    agent = QLearningAgent(symbol='X',
                           learning_rate=learning_rate,
                           discount_factor=discount_factor,
                           epsilon=epsilon_start,
                           training_mode=True)

    # Training statistics
    wins = 0
    losses = 0
    draws = 0
    epsilon = epsilon_start

    print("Starting training...\n")

    for episode in range(1, n_episodes + 1):
        # Update epsilon (decay exploration over time)
        epsilon = max(epsilon_end, epsilon * epsilon_decay)
        agent.set_epsilon(epsilon)

        # Alternate who goes first
        agent_first = random.choice([True, False])

        # Train against random opponent
        result = play_training_game(agent,
                                    opponent_type='random',
                                    agent_first=agent_first)

        # Update statistics
        if result == 'win':
            wins += 1
        elif result == 'loss':
            losses += 1
        else:
            draws += 1

        # Print progress
        if episode % eval_every == 0:
            total = wins + losses + draws
            win_rate = wins / total * 100
            loss_rate = losses / total * 100
            draw_rate = draws / total * 100

            stats = agent.get_stats()

            print(f"Episode {episode}/{n_episodes}")
            print(f"  Epsilon: {epsilon:.4f}")
            print(
                f"  Win rate: {win_rate:.1f}% | Loss rate: {loss_rate:.1f}% | Draw rate: {draw_rate:.1f}%"
            )
            print(
                f"  Q-table size: {stats['total_entries']} entries, {stats['unique_states']} states"
            )
            print(f"  Avg Q-value: {stats['avg_q_value']:.3f}")
            print()

            # Reset counters for next interval
            wins = losses = draws = 0

    # Save the trained Q-table to the training directory
    print("=" * 60)
    print("Training complete!")
    print("=" * 60)

    # Save to training directory (where this script is located)
    script_dir = Path(__file__).parent
    save_path = script_dir / save_file
    agent.save(str(save_path))
    print(f"Q-table saved to: {save_path}")

    # Final evaluation
    print("\nFinal Evaluation (1000 games, no exploration)...")
    agent.set_training_mode(False)
    agent.set_epsilon(0.0)

    wins = losses = draws = 0
    for _ in range(1000):
        agent_first = random.choice([True, False])
        result = play_training_game(agent,
                                    opponent_type='random',
                                    agent_first=agent_first)
        if result == 'win':
            wins += 1
        elif result == 'loss':
            losses += 1
        else:
            draws += 1

    print(f"\nFinal Results (vs Random opponent):")
    print(f"  Wins: {wins}/1000 ({wins/10:.1f}%)")
    print(f"  Losses: {losses}/1000 ({losses/10:.1f}%)")
    print(f"  Draws: {draws}/1000 ({draws/10:.1f}%)")

    final_stats = agent.get_stats()
    print(f"\nFinal Q-table statistics:")
    print(f"  Total entries: {final_stats['total_entries']}")
    print(f"  Unique states: {final_stats['unique_states']}")
    print(f"  Average Q-value: {final_stats['avg_q_value']:.3f}")


if __name__ == "__main__":
    # Train the agent
    train_agent(n_episodes=50000,
                learning_rate=0.1,
                discount_factor=0.9,
                epsilon_start=1.0,
                epsilon_end=0.01,
                epsilon_decay=0.9995,
                eval_every=5000,
                save_file="q_table.pkl")
