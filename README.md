# Tic-Tac-Toe
## From Basic Python to Machine Learning

A complete educational project that progresses from basic Python implementations to Reinforcement Learning, using the classic Tic-Tac-Toe game.

## 🎯 Project Objective

This repository is designed to teach programming progressively:

1. **Python Fundamentals** - Basic data structures
2. **Game Algorithms** - Minimax and game theory
3. **Software Design** - Object-oriented programming
4. **Machine Learning** - Q-Learning and reinforcement learning

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
├── 03_oop/                 # 🏗️ Object-oriented version
│   ├── main.py
│   ├── game_board.py
│   ├── player.py
│   └── README.md
│
└── 04_qlearning/           # 🤖 Q-Learning (RL)
    ├── theory/             # Educational notebooks
    ├── training/           # Train agent
    ├── standalone/         # Standalone game
    ├── oop_integration/    # Integration with 03_oop
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

---

### Level 4: Machine Learning
**Folder:** [`04_qlearning/`](04_qlearning/)

Build an agent that learns by itself using Reinforcement Learning:
- Q-Learning algorithm
- Bellman equation
- Exploration vs Exploitation
- Agent training
- Integration with existing code

**Learning path:**

1. **Theory** (2 hours)
   ```bash
   cd 04_qlearning/theory
   jupyter notebook tictactoe_qlearning.ipynb
   ```

2. **Train your agent** (10 minutes)
   ```bash
   cd 04_qlearning/training
   python3 train_qlearning.py
   ```

3. **Play against the agent** (∞ hours of fun)
   ```bash
   cd 04_qlearning/standalone
   python3 ttt_qlearning.py
   ```

4. **Integrate with OOP**
   ```bash
   cd 04_qlearning/oop_integration
   python3 main.py
   # Select option 3: Q-Learning
   ```

**Expected results:**
- Win rate: 83.5% vs random
- Q-table: ~12,500 entries
- Learns winning strategies automatically

## 🎮 Quick Gameplay

Just want to play? Choose your level:

```bash
# Easy - Random opponent
python3 03_oop/main.py  # Option 1

# Impossible - Perfect Minimax
python3 03_oop/main.py  # Option 2

# Hard - Trained agent (Q-Learning)
python3 04_qlearning/standalone/ttt_qlearning.py

```

## 📊 Approach Comparison

| Aspect | Basic | Minimax | Q-Learning |
|---------|--------|---------|------------|
| **Complexity** | Low | Medium | High |
| **Performance** | Poor (~50%) | Optimal (100%) | Very good (~85%) |
| **Learns** | No | No | Yes |
| **Requires rules** | Yes | Yes | No |
| **Code** | 50 lines | 100 lines | 300 lines |
| **Extendable to other games** | No | With modifications | Yes |

## 🛠️ Requirements

### Basic (01-03)
```bash
python3 --version  # Python 3.7+
```

### Machine Learning (04)
```bash
pip install -r 04_qlearning/requirements.txt
```

Dependencies:
- `numpy` - Numerical operations
- `jupyter` - Interactive notebooks
- `matplotlib` - Visualizations

## 📈 Complexity Progression

```
01_basics:     ▓░░░░ (1/5) - Variables, loops, functions
02_minimax:    ▓▓░░░ (2/5) - Recursion, algorithms
03_oop:        ▓▓▓░░ (3/5) - Classes, design
04_qlearning:  ▓▓▓▓▓ (5/5) - Machine learning, AI
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

### 04 - Q-Learning
- ✅ Reinforcement Learning
- ✅ Q-Learning algorithm
- ✅ Bellman equation
- ✅ Exploration vs Exploitation
- ✅ Agent training
- ✅ Performance evaluation


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

### Q-Learning
- [ ] Train against Minimax
- [ ] Implement self-play
- [ ] Explore different hyperparameters
- [ ] Visualize Q-values in real-time
- [ ] Implement DQN (Deep Q-Network)


## 📝 Notes

### Why Tic-Tac-Toe?
- ✅ Everyone knows it
- ✅ Simple rules
- ✅ Small state space (3^9 = 19,683)
- ✅ Visible results
- ✅ Quick to implement


## 🔮 Next Steps

After completing this project, you can:

1. **More complex games**: Connect Four, Checkers, Chess
2. **Deep RL**: Implement DQN with PyTorch/TensorFlow
3. **Multi-agent**: Multiple competing agents
4. **Transfer Learning**: Reuse Q-table for other games
5. **Production**: Deploy as web app

