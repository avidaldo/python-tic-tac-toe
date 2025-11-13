# 03 - Object-Oriented Version (OOP)

This folder contains an object-oriented implementation of Tic-Tac-Toe, applying software design and architecture principles.

## Project Structure

```
03_oop/
├── main.py              # Entry point
├── ttt_game.py          # Game logic
├── game_board.py        # Board
├── player.py            # Players (abstract + concrete)
├── symbol.py            # Symbols (X, O)
└── game_messages.py     # Game messages
```

## Architecture

### 📋 [game_board.py](game_board.py)
**GameBoard Class** - Represents the board

Responsibilities:
- Maintain board state
- Validate moves
- Detect winner
- Print the board

```python
board = GameBoard()
board[5] = Symbol.X
winner = board.check_winner()
```

### 👤 [player.py](player.py)
**Player Hierarchy** - Strategy Pattern

```
Player (ABC)
├── HumanPlayer
└── MachinePlayer (ABC)
    ├── RandomMachinePlayer
    └── MinimaxMachinePlayer
```

**Benefits:**
- Easy to add new player types
- Common interface: `make_move(board)`
- Polymorphism in action

### 🎮 [ttt_game.py](ttt_game.py)
**TicTacToeGame Class** - Orchestrates game flow

Responsibilities:
- Configure players
- Manage turns
- Detect end of game
- Show results

### 🔤 [symbol.py](symbol.py)
**Symbol Enum** - Game symbols

```python
class Symbol(Enum):
    HUMAN = 'O'
    AI = 'X'
```

### 💬 [game_messages.py](game_messages.py)
**GameMessages Class** - Centralizes messages

Benefits:
- Easy translation
- Simple maintenance
- Single place for texts

## Applied OOP Principles

### 1. **Encapsulation**
Each class has well-defined responsibilities:
```python
board = GameBoard()  # Manages the board
player = MinimaxMachinePlayer(Symbol.AI)  # Plays
```

### 2. **Abstraction**
Abstract classes define interfaces:
```python
class Player(ABC):
    @abstractmethod
    def make_move(self, board):
        pass
```

### 3. **Inheritance**
Code reuse:
```python
class MinimaxMachinePlayer(MachinePlayer):
    def _select_move(self, board):
        # Minimax specific logic
```

### 4. **Polymorphism**
Same method, different behaviors:
```python
players[Symbol.HUMAN].make_move(board)  # User input
players[Symbol.AI].make_move(board)     # AI algorithm
```

## Design Patterns

### Strategy Pattern
Different interchangeable AI algorithms:
- `RandomMachinePlayer`: Random moves
- `MinimaxMachinePlayer`: Minimax algorithm

### Template Method Pattern
`MachinePlayer` defines structure, subclasses implement `_select_move()`.

## How to Run

```bash
python3 main.py
```

**Options:**
1. Choose difficulty: Random (1) or Minimax (2)
2. Choose who starts: Human (1) or AI (2)
3. Play!

## Comparison with Previous Versions

| Aspect | Basic Version | OOP Version |
|---------|----------------|-------------|
| Structure | Loose functions | Organized classes |
| Scalability | Hard to add features | Easy extension |
| Maintenance | Coupled code | Low coupling |
| Testability | Difficult | Easy (mocks, etc.) |
| Readability | Less clear | Very clear |

## Advantages of this Architecture

✅ **Extensible**: Easy to add new players (e.g., Q-Learning)
✅ **Testable**: Each class can be tested independently
✅ **Maintainable**: Localized changes, low impact
✅ **Readable**: Self-documenting code
✅ **Professional**: Industry standards

## Suggested Exercises

1. **Add medium difficulty**: Minimax with limited depth
2. **Add GUI**: Graphical interface with Tkinter
3. **Implement undo**: Move stack
4. **Add statistics**: Wins/losses/draws
5. **Save/load game**: Serialization

