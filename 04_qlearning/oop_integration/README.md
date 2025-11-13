# Q-Learning Integration with OOP Version

This folder shows how to integrate the Q-Learning agent with the object-oriented architecture of the [03_oop](../../03_oop/) project.

## 🎯 Objective

Add the Q-Learning agent as another AI option, maintaining a clean and extensible architecture.

## 📁 Files

### [q_learning_player.py](q_learning_player.py)
**QLearningMachinePlayer Class**

Adapter that allows using the Q-Learning agent with the OOP player interface.

```python
class QLearningMachinePlayer:
    def __init__(self, symbol, q_table_path=None):
        # Loads the trained agent
        self.agent = QLearningAgent(...)

    def make_move(self, board):
        # Interface compatible with other players
        move = self._select_move(board)
        board[move] = self.symbol
```

### [main.py](main.py)
**OOP Game with Q-Learning Option**

Modified version of `03_oop/main.py` that adds Q-Learning as third option.

## 🔧 How It Works

### 1. Extended Player Hierarchy

```
Before (03_oop/player.py):
├── Player (ABC)
    ├── HumanPlayer
    └── MachinePlayer (ABC)
        ├── RandomMachinePlayer
        └── MinimaxMachinePlayer

Now (with Q-Learning):
├── Player (ABC)
    ├── HumanPlayer
    ├── MachinePlayer (ABC)
    │   ├── RandomMachinePlayer
    │   └── MinimaxMachinePlayer
    └── QLearningMachinePlayer  ← NEW!
```

**Note:** `QLearningMachinePlayer` doesn't inherit from `MachinePlayer` because it uses a different internal structure (the Q-Learning agent), but follows the same interface.

### 2. Interface Adapter

`QLearningMachinePlayer` acts as an **adapter** (design pattern):

```python
# GameBoard uses indices 1-9 and Symbol enum
board[5] = Symbol.X

# QLearningAgent expects dictionaries with strings
board_dict = {1: 'X', 2: None, ..., 9: None}

# The adapter converts between both formats
class QLearningMachinePlayer:
    def _select_move(self, board):
        # Converts GameBoard → dict
        board_dict = self._convert_board(board)

        # Gets move from agent
        move = self.agent.choose_action(board_dict, available)

        return move
```

### 3. Automatic Q-Table Loading

```python
# Automatically searches for the trained Q-table
default_path = '../training/q_table.pkl'

# Or specify custom path
player = QLearningMachinePlayer(
    symbol=Symbol.AI,
    q_table_path='my_q_table.pkl'
)
```

## 🚀 Usage

### Run the Game

**Important:** Run as a Python module from the project root directory:

```bash
# From the project root (python-tic-tac-toe/)
python3 -m 04_qlearning.oop_integration.main
```

### Menu Options

```
Select AI opponent:
  1. Random (Easy)
  2. Minimax (Impossible to beat)
  3. Q-Learning (Trained agent)  ← NEW!

Your choice (1/2/3): 3
```

### Example Session

```
============================================================
  TIC-TAC-TOE with Q-Learning
============================================================

Select AI opponent:
  1. Random (Easy)
  2. Minimax (Impossible to beat)
  3. Q-Learning (Trained agent)

Your choice (1/2/3): 3

Q-table loaded from ../training/q_table.pkl
Total state-action pairs: 12517
Q-learning agent loaded successfully

Who goes first (1=Human, 2=AI)? 1

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
...
```

## 🛠️ Detailed Implementation

### Step 1: Import Dependencies

```python
# main.py
import sys
import os

# Add path for external 03_oop dependency
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '03_oop'))

# Import from 03_oop
from game_board import GameBoard
from player import HumanPlayer
from game_messages import GameMessages
from symbol import Symbol

# Import using relative import (no sys.path needed)
from .q_learning_player import QLearningMachinePlayer
```

### Step 2: Extend the Options

```python
# ttt_game.py (modified)
class TicTacToeGame:
    RANDOM = '1'
    MINIMAX = '2'
    QLEARNING = '3'  # ← New constant

    def prompt_select_difficulty(self):
        print("Select AI opponent:")
        print("  1. Random")
        print("  2. Minimax")
        print("  3. Q-Learning")  # ← New option

        choice = input("Your choice: ")
        if choice == self.QLEARNING:
            return QLearningMachinePlayer
        # ...
```

### Step 3: Format Conversion

```python
# q_learning_player.py
def _convert_board_to_dict(self, board):
    """Converts GameBoard to agent format."""
    board_dict = {}
    for i in range(1, 10):
        cell_value = board[i]
        if cell_value is not None:
            # Converts Symbol enum to string
            board_dict[i] = str(cell_value.value)
        else:
            board_dict[i] = None
    return board_dict
```

## 🎨 Applied Design Patterns

### 1. **Adapter Pattern**
`QLearningMachinePlayer` adapts the Q-Learning agent interface to the interface expected by the OOP game.

```python
# Interface expected by the game
player.make_move(board)

# Q-Learning agent interface
agent.choose_action(board_dict, available)

# The adapter joins both
class QLearningMachinePlayer:
    def make_move(self, board):
        board_dict = self._convert(board)
        move = self.agent.choose_action(board_dict, ...)
        board[move] = self.symbol
```

### 2. **Strategy Pattern**
Different interchangeable AI algorithms:

```python
players = {
    Symbol.AI: strategy_class(Symbol.AI)
}

# strategy_class can be:
# - RandomMachinePlayer
# - MinimaxMachinePlayer
# - QLearningMachinePlayer
```

### 3. **Facade Pattern**
`QLearningMachinePlayer` hides the complexity of the Q-Learning agent behind a simple interface.

## ✅ Advantages of this Integration

1. **Doesn't modify original code**: `03_oop/` remains intact
2. **Easy to maintain**: Changes in Q-Learning don't affect OOP
3. **Extensible**: Easy to add more agent types
4. **Testable**: Each component can be tested independently
5. **Reusable**: The Q-Learning agent works standalone or integrated

## 🔍 Strategy Comparison

### In the Same Game

Now you can compare the three approaches:

```bash
# From the project root
python3 -m 04_qlearning.oop_integration.main

# Game 1: vs Random (Option 1)
# Result: Easy to win

# Game 2: vs Minimax (Option 2)
# Result: Impossible to win (optimal draw)

# Game 3: vs Q-Learning (Option 3)
# Result: Hard to win (plays very well)
```

### Expected Performance

| Opponent | Win Rate (Human) | Difficulty |
|----------|-------------------|------------|
| Random | ~80% | ⭐ Easy |
| Q-Learning | ~15% | ⭐⭐⭐ Hard |
| Minimax | 0% | ⭐⭐⭐⭐ Impossible |

## 🧪 Testing

### Manual Test

```bash
# From the project root
# 1. Verify Q-table loads
python3 -m 04_qlearning.oop_integration.main
# Should show: "Q-table loaded from ..."

# 2. Play and observe intelligent moves
# The agent should:
# - Block opponent's winning moves
# - Seek to win when possible
# - Play corners/center preferentially
```

### Integration Test

```python
# test_integration.py (example)
from q_learning_player import QLearningMachinePlayer
from game_board import GameBoard
from symbol import Symbol

board = GameBoard()
player = QLearningMachinePlayer(Symbol.AI)

# Verify interface
player.make_move(board)
assert board.check_winner() is None  # Valid move
```

## 📊 Comparison: Standalone vs Integrated

### Standalone ([standalone/ttt_qlearning.py](../standalone/ttt_qlearning.py))

**Pros:**
- Independent, easy to distribute
- Doesn't require other project files
- CLI interface specific to Q-Learning

**Cons:**
- Duplicated code (game logic repeated)
- Doesn't leverage existing OOP architecture

### Integrated (this directory)

**Pros:**
- Reuses existing OOP code
- Direct strategy comparison
- Maintains consistent architecture
- More professional and maintainable

**Cons:**
- Depends on multiple directories
- Requires understanding OOP architecture

## 🚀 Next Steps

### 1. Add More Agents

```python
# Example: DQN agent (Deep Q-Network)
class DQNMachinePlayer:
    def __init__(self, symbol, model_path):
        self.model = load_model(model_path)

    def make_move(self, board):
        # Uses neural network instead of Q-table
        ...
```

### 2. Agent Tournament

```python
# tournament.py
agents = [
    RandomMachinePlayer,
    MinimaxMachinePlayer,
    QLearningMachinePlayer
]

results = run_tournament(agents, n_games=1000)
print_results(results)
```

### 3. Mix Strategies

```python
# Hybrid agent
class HybridPlayer:
    def make_move(self, board):
        if early_game:
            return qlearning_move(board)
        else:
            return minimax_move(board)
```

## 📚 Resources

- [Adapter Pattern](https://refactoring.guru/design-patterns/adapter)
- [Strategy Pattern](https://refactoring.guru/design-patterns/strategy)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)

## 💡 Conclusion

This integration demonstrates how to apply software design principles to combine different technologies (classic algorithms + machine learning) in a clean and extensible architecture.

**Key lessons:**
- Common interfaces allow component interchange
- Adapters join different technologies
- Modular design facilitates maintenance
- Well-structured code is more valuable than fast code

Now you have 3 difficulty levels in one game! 🎮
