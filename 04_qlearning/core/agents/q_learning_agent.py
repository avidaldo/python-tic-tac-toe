"""
Q-Learning Agent for Tic-Tac-Toe

This module implements a Reinforcement Learning agent that learns to play
tic-tac-toe using the Q-learning algorithm.
"""

import numpy as np
import random
import pickle


class QLearningAgent:
    """
    A Q-Learning agent that learns optimal tic-tac-toe strategy through
    trial and error.

    The agent maintains a Q-table that maps (state, action) pairs to
    expected future rewards. Through training, it learns which moves
    lead to wins, losses, or draws.
    """

    def __init__(self, symbol='X', learning_rate=0.1, discount_factor=0.9,
                 epsilon=0.1, training_mode=True):
        """
        Initialize the Q-Learning agent.

        Args:
            symbol: The player's symbol ('X' or 'O')
            learning_rate (α): How much to update Q-values (0-1)
            discount_factor (γ): How much to value future rewards (0-1)
            epsilon (ε): Exploration rate for epsilon-greedy policy (0-1)
            training_mode: If True, agent explores; if False, uses greedy policy
        """
        self.symbol = symbol
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.training_mode = training_mode

        # Q-table: dictionary mapping (state, action) -> Q-value
        # state: tuple of 9 values representing board configuration
        # action: integer 1-9 representing cell position
        self.q_table = {}

        # Track the history of (state, action) pairs in current episode
        self.episode_history = []

    def get_state_key(self, board):
        """
        Convert board dictionary to a hashable tuple for Q-table lookup.

        Args:
            board: Dictionary with keys 1-9, values None, 'X', or 'O'

        Returns:
            Tuple of 9 values representing the board state
        """
        return tuple(board.get(i, None) for i in range(1, 10))

    def get_q_value(self, state, action):
        """
        Get Q-value for a state-action pair.

        Args:
            state: Board state as tuple
            action: Action (cell position 1-9)

        Returns:
            Q-value, or 0.0 if never seen before
        """
        return self.q_table.get((state, action), 0.0)

    def set_q_value(self, state, action, value):
        """
        Set Q-value for a state-action pair.

        Args:
            state: Board state as tuple
            action: Action (cell position 1-9)
            value: New Q-value
        """
        self.q_table[(state, action)] = value

    def choose_action(self, board, available_actions):
        """
        Choose an action using epsilon-greedy policy.

        During training:
        - With probability epsilon: explore (random action)
        - With probability 1-epsilon: exploit (best known action)

        During play (not training):
        - Always choose best action (greedy policy)

        Args:
            board: Current board state
            available_actions: List of available cell positions

        Returns:
            Chosen action (cell position 1-9)
        """
        state = self.get_state_key(board)

        # Epsilon-greedy: explore vs exploit
        if self.training_mode and random.random() < self.epsilon:
            # Explore: choose random action
            action = random.choice(available_actions)
        else:
            # Exploit: choose action with highest Q-value
            q_values = {
                action: self.get_q_value(state, action)
                for action in available_actions
            }
            max_q = max(q_values.values())

            # If multiple actions have same max Q-value, choose randomly among them
            best_actions = [a for a, q in q_values.items() if q == max_q]
            action = random.choice(best_actions)

        # Record this state-action pair for learning
        if self.training_mode:
            self.episode_history.append((state, action))

        return action

    def learn(self, reward, next_board=None):
        """
        Update Q-value using Q-learning formula (Bellman equation).

        Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') - Q(s,a)]

        This single method handles BOTH cases:
        - Game continues: next_board is a dict, we calculate max future Q-value
        - Game ends: next_board is None, so max_future_q = 0 (terminal state)

        Args:
            reward: Immediate reward received
                   - Final rewards: +1.0 (win), -1.0 (loss), 0.0 (draw)
                   - Intermediate: -0.01 (small penalty per move)
            next_board: Resulting board state after the action.
                       - If None: Game ended (terminal state)
                       - If dict: Game continues (non-terminal state)
        """
        if not self.training_mode or not self.episode_history:
            return

        # Get the last state-action pair
        state, action = self.episode_history[-1]

        # Current Q-value
        current_q = self.get_q_value(state, action)

        # Calculate best future Q-value
        if next_board is None:
            # TERMINAL STATE: Game ended, no future rewards possible
            max_future_q = 0.0
        else:
            # NON-TERMINAL STATE: Game continues
            # Find max Q-value from next state
            next_state = self.get_state_key(next_board)
            next_actions = [i for i in range(1, 10) if next_board.get(i) is None]

            if next_actions:
                max_future_q = max(
                    self.get_q_value(next_state, a) for a in next_actions)
            else:
                max_future_q = 0.0

        # Q-LEARNING UPDATE FORMULA (Bellman Equation)
        # Q(s,a) ← Q(s,a) + α[r + γ·max Q(s',a') - Q(s,a)]
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_future_q - current_q)

        self.set_q_value(state, action, new_q)

    def reset_episode(self):
        """Reset the episode history for a new game."""
        self.episode_history = []

    def save(self, filename):
        """
        Save the Q-table to a file.

        Args:
            filename: Path to save file
        """
        with open(filename, 'wb') as f:
            pickle.dump(self.q_table, f)
        print(f"Q-table saved to {filename}")
        print(f"Total state-action pairs learned: {len(self.q_table)}")

    def load(self, filename):
        """
        Load Q-table from a file.

        Args:
            filename: Path to load file
        """
        try:
            with open(filename, 'rb') as f:
                self.q_table = pickle.load(f)
            print(f"Q-table loaded from {filename}")
            print(f"Total state-action pairs: {len(self.q_table)}")
        except FileNotFoundError:
            print(f"No saved Q-table found at {filename}")
            print("Starting with empty Q-table")

    def set_training_mode(self, training):
        """Enable or disable training mode."""
        self.training_mode = training

    def set_epsilon(self, epsilon):
        """Update exploration rate."""
        self.epsilon = epsilon

    def get_stats(self):
        """
        Get statistics about the Q-table.

        Returns:
            Dictionary with Q-table statistics
        """
        if not self.q_table:
            return {
                'total_entries': 0,
                'unique_states': 0,
                'avg_q_value': 0.0,
                'max_q_value': 0.0,
                'min_q_value': 0.0
            }

        values = list(self.q_table.values())
        states = set(state for state, _ in self.q_table.keys())

        return {
            'total_entries': len(self.q_table),
            'unique_states': len(states),
            'avg_q_value': np.mean(values),
            'max_q_value': np.max(values),
            'min_q_value': np.min(values)
        }
