"""
Training Script for the Q-Learning Tic-Tac-Toe Agent

Trains with canonical self-play (notebook 05): two agents share one Q-table whose states are
written from the point of view of the player to move, so the resulting table can play as X or O.
"""

import random
from pathlib import Path

from ..core.environment import TicTacToeEnvironment
from ..core.agents.q_learning_agent import QLearningAgent
from ..core.agents.random_agent import RandomAgent
from ..core.agents.minimax_agent import MinimaxAgent
from ..core.training import play_game, evaluate_agent

Q_TABLE_PATH = Path(__file__).parent / 'q_table.pkl'


def train_agent(n_episodes: int = 20000, learning_rate: float = 0.1, discount_factor: float = 0.9,
                epsilon_start: float = 1.0, epsilon_end: float = 0.05, epsilon_decay: float = 0.9995,
                report_every: int = 2000) -> QLearningAgent:
    """Train two canonical agents sharing one Q-table and return the one playing X."""
    print("=" * 60)
    print("  Training Q-Learning Agent for Tic-Tac-Toe (canonical self-play)")
    print("=" * 60)
    print(f"  Episodes: {n_episodes}")
    print(f"  Learning rate (α): {learning_rate}")
    print(f"  Discount factor (γ): {discount_factor}")
    print(f"  Epsilon: {epsilon_start} → {epsilon_end} (decay: {epsilon_decay})\n")

    shared_q_table: dict = {}
    agent_x, agent_o = (QLearningAgent(symbol=symbol, learning_rate=learning_rate, discount_factor=discount_factor,
                                       epsilon=epsilon_start, q_table=shared_q_table, canonical_state=True)
                        for symbol in ('X', 'O'))
    env = TicTacToeEnvironment()
    epsilon = epsilon_start
    results = {'X': 0, 'O': 0, 'draw': 0}

    for episode in range(1, n_episodes + 1):
        epsilon = max(epsilon_end, epsilon * epsilon_decay)
        agent_x.set_epsilon(epsilon)
        agent_o.set_epsilon(epsilon)

        result = play_game(agent_x, agent_o, env, x_starts=random.choice([True, False]))
        results[result] += 1

        if episode % report_every == 0:
            print(f"Episode {episode}/{n_episodes} | ε={epsilon:.3f} | "
                  f"X wins {results['X'] / report_every:.2f} | O wins {results['O'] / report_every:.2f} | "
                  f"draws {results['draw'] / report_every:.2f} | Q-table {len(shared_q_table)} entries")
            results = {'X': 0, 'O': 0, 'draw': 0}

    return agent_x


def main() -> None:
    agent = train_agent()
    agent.save(str(Q_TABLE_PATH))

    print("\nFinal evaluation (no exploration, random starter):")
    for opponent_name, opponent, n_games in (('Random', RandomAgent('O'), 1000), ('Minimax', MinimaxAgent('O'), 200)):
        result = evaluate_agent(agent, opponent, n_games)
        print(f"  vs {opponent_name:7} ({n_games} games): win {result['win_rate']:.1%} | "
              f"loss {result['loss_rate']:.1%} | draw {result['draw_rate']:.1%}")


if __name__ == "__main__":
    main()
