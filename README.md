# Tic-Tac-Toe
## From Basic Python to Object-Oriented Design

An educational project that uses the classic Tic-Tac-Toe game to go from basic Python to a game-playing
algorithm (Minimax) and an object-oriented design.

## 🎯 Project Objective

This repository is designed to teach programming progressively:

1. **Python Fundamentals** - Basic data structures
2. **Game Algorithms** - Minimax and game theory
3. **Software Design** - Object-oriented programming

Each section is independent but builds on previous concepts.

## 📚 Repository Structure

```
python-tic-tac-toe/
│
├── 01_basics/              # 🎓 Basic implementations
│   ├── ttt_v11_list_of_lists.py
│   ├── ttt_v12_dict.py
│   └── README.md
│
├── 02_minimax/             # 🧠 Minimax Algorithm
│   ├── ttt_v13a_minimax.py
│   ├── ttt_v13b_minimax.py
│   ├── MINIMAX_ALGORITHM.md
│   └── README.md
│
└── 03_oop/                 # 🏗️ Object-oriented version
    ├── main.py
    ├── game_board.py
    ├── player.py
    └── README.md
```

## 🚀 Learning Guide

### Level 1: Python Fundamentals
**Folder:** [`01_basics/`](01_basics/)

Learn basic data structures by implementing Tic-Tac-Toe:
- List of lists (matrices)
- Dictionaries
- Loops and conditionals
- Functions

**Start here:**
```bash
cd 01_basics
python3 ttt_v12_dict.py
```

**Concepts:** Variables, lists, dictionaries, functions, input/output

---

### Level 2: AI Algorithms
**Folder:** [`02_minimax/`](02_minimax/)

Implement unbeatable AI using the Minimax algorithm:
- Decision trees
- Advanced recursion
- State evaluation
- Game theory

**Read first:** [`MINIMAX_ALGORITHM.md`](02_minimax/MINIMAX_ALGORITHM.md)

**Run:**
```bash
cd 02_minimax
python3 ttt_v13a_minimax.py
```

**Challenge:** Can you beat the AI? (Spoiler: It's impossible 😄)

---

### Level 3: Software Design
**Folder:** [`03_oop/`](03_oop/)

Learn object-oriented programming with professional architecture:
- Classes and objects
- Inheritance and polymorphism
- Design patterns (Strategy, Template Method)
- SOLID principles
- Clean and maintainable code

**Run:**
```bash
cd 03_oop
python3 main.py
```

**Architecture:**
```
GameBoard     →  Manages board
Player (ABC)  →  Common interface
├── HumanPlayer
└── MachinePlayer
    ├── Random
    └── Minimax
```

## 🎮 Quick Gameplay

Just want to play? Choose your level:

```bash
# Easy - Random opponent
python3 03_oop/main.py  # Option 1

# Impossible - Perfect Minimax
python3 03_oop/main.py  # Option 2
```

## 📊 Approach Comparison

| Aspect | Basic | Minimax |
|---------|--------|---------|
| **Complexity** | Low | Medium |
| **Performance** | Poor (~50%) | Optimal |
| **Code** | 50 lines | 100 lines |
| **Extendable to other games** | No | With modifications |

## 🛠️ Requirements

```bash
python3 --version  # Python 3.7+
```

No external dependencies are needed.

## 📈 Complexity Progression

```
01_basics:     ▓░░░░ (1/5) - Variables, loops, functions
02_minimax:    ▓▓░░░ (2/5) - Recursion, algorithms
03_oop:        ▓▓▓░░ (3/5) - Classes, design
```

## 🎓 Concepts Taught

### 01 - Basics
- ✅ Data structures (lists, dictionaries)
- ✅ Control flow (if, while, for)
- ✅ Functions and modularity
- ✅ Input/output handling

### 02 - Minimax
- ✅ Advanced recursion
- ✅ Decision trees
- ✅ Search algorithms
- ✅ Optimization (alpha-beta pruning)
- ✅ Game theory

### 03 - OOP
- ✅ Classes and objects
- ✅ Inheritance and composition
- ✅ Abstraction and encapsulation
- ✅ Polymorphism
- ✅ Design patterns
- ✅ SOLID principles

## 🔬 Suggested Experiments

### Basic
- [ ] Add input validation
- [ ] Implement larger boards (4x4)
- [ ] Add colors to interface

### Minimax
- [ ] Implement alpha-beta pruning
- [ ] Add limited depth
- [ ] Measure execution time

### OOP
- [ ] Add GUI with Tkinter
- [ ] Implement undo/redo
- [ ] Save/load games
- [ ] Add statistics

## 📝 Notes

### Why Tic-Tac-Toe?
- ✅ Everyone knows it
- ✅ Simple rules
- ✅ Small state space (3^9 = 19,683)
- ✅ Visible results
- ✅ Quick to implement


## 🔮 Next Steps

After completing this project, you can:

1. **Reinforcement Learning**: [tictactoe-qlearning](https://github.com/avidaldo/tictactoe-qlearning) trains an agent that learns to play by itself
   (Q-learning), and compares it against the Minimax player from `02_minimax`
2. **More complex games**: Connect Four, Checkers, Chess
3. **Production**: Deploy as web app

