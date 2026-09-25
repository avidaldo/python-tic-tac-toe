"""
Game loop, evaluation and plotting helpers shared by the notebooks and the CLI scripts.
"""

import random

import matplotlib.pyplot as plt

from .environment import TicTacToeEnvironment
from .agents.agent import Agent
from .agents.q_learning_agent import QLearningAgent

STEP_REWARD = -0.01


def terminal_reward(result: str | None, symbol: str) -> float:
    """Final reward from the point of view of the player using `symbol`."""
    if result == symbol:
        return 1.0
    if result == 'draw':
        return 0.0
    return -1.0


def play_game(agent_x: Agent, agent_o: Agent, env: TicTacToeEnvironment, x_starts: bool = True) -> str | None:
    """
    Play one game between two agents, letting every Q-learning agent learn from it.

    From a learner's point of view the opponent is part of the environment, so the transition
    started by its move only ends when it is its turn again (after the opponent's reply), or when
    the game ends. That is when each Q-learning update happens:

    - At the start of an agent's turn, its previous (state, action) is updated with the current
      board as next state, a board where that agent is to move.
    - When the game ends, both agents update their pending (state, action) with the final reward.

    Args:
        agent_x: Agent playing X
        agent_o: Agent playing O
        env: The game environment
        x_starts: If True, X plays first

    Returns:
        'X', 'O', or 'draw'
    """
    env.reset()
    learners = [agent for agent in (agent_x, agent_o) if isinstance(agent, QLearningAgent)]
    for learner in learners:
        learner.reset_episode()

    current_agent, waiting_agent = (agent_x, agent_o) if x_starts else (agent_o, agent_x)

    while True:
        # The opponent has replied: the transition started by our previous move ends here
        if isinstance(current_agent, QLearningAgent):
            current_agent.learn(reward=STEP_REWARD, next_board=env.board)

        move = current_agent.choose_action(env.board, env.get_available_actions())
        env.make_move(move, current_agent.symbol)

        is_over, result = env.is_game_over()
        if is_over:
            for learner in learners:
                learner.learn(reward=terminal_reward(result, learner.symbol), next_board=None)
            return result

        current_agent, waiting_agent = waiting_agent, current_agent


def evaluate_agent(agent: Agent, opponent: Agent, n_games: int = 1000) -> dict[str, float]:
    """
    Evaluate an agent against a specific opponent, with learning and exploration switched off.

    Args:
        agent: The agent to evaluate
        opponent: The opponent agent instance (e.g. RandomAgent(), MinimaxAgent())
        n_games: Number of games to play; who starts is chosen at random each game

    Returns:
        Win/loss/draw counts and rates from `agent`'s point of view.
    """
    original_modes = {id(player): player.training_mode
                      for player in (agent, opponent) if isinstance(player, QLearningAgent)}
    for player in (agent, opponent):
        if isinstance(player, QLearningAgent):
            player.set_training_mode(False)

    agent_x, agent_o = (agent, opponent) if agent.symbol == 'X' else (opponent, agent)
    env = TicTacToeEnvironment()
    wins = losses = draws = 0

    for _ in range(n_games):
        result = play_game(agent_x, agent_o, env, x_starts=random.choice([True, False]))
        if result == agent.symbol:
            wins += 1
        elif result == 'draw':
            draws += 1
        else:
            losses += 1

    for player in (agent, opponent):
        if isinstance(player, QLearningAgent):
            player.set_training_mode(original_modes[id(player)])

    return {
        'wins': wins,
        'losses': losses,
        'draws': draws,
        'win_rate': wins / n_games,
        'loss_rate': losses / n_games,
        'draw_rate': draws / n_games,
    }


def plot_training_history(history: dict[str, list[float]], eval_every: int, title: str = "Training History") -> None:
    """
    Plot result rates and epsilon decay recorded every `eval_every` episodes.

    `history` holds either 'wins'/'losses'/'draws' (one learner) or 'x_wins'/'o_wins'/'draws'
    (self-play), plus optionally 'epsilon'.
    """
    result_keys = ['x_wins', 'o_wins', 'draws'] if 'x_wins' in history else ['wins', 'losses', 'draws']
    episodes = [eval_every * i for i in range(1, len(history['draws']) + 1)]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    for key in result_keys:
        axes[0].plot(episodes, history[key], label=key.replace('_', ' ').capitalize())
    axes[0].set_title(f"{title} - Results")
    axes[0].set_xlabel("Episode")
    axes[0].set_ylabel("Rate")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    if 'epsilon' in history:
        axes[1].plot(episodes, history['epsilon'], color='purple', label='Epsilon')
        axes[1].set_title("Exploration Rate (Epsilon)")
        axes[1].set_xlabel("Episode")
        axes[1].set_ylabel("Epsilon")
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()
