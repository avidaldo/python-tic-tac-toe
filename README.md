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
    ├── notebooks/          # Step-by-step notebooks (01 basics → 06 tuning)
    ├── core/               # Shared environment, agents and training loop
    ├── standalone/         # Train and play from the command line
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
- Training in a turn-based (two-player) game
- Training opponents: random, Minimax, self-play
- Hyperparameter search
- Integration with existing code

**Learning path:**

1. **Notebooks** `04_qlearning/notebooks/01` → `06`, in order (see [`04_qlearning/README.md`](04_qlearning/README.md))

2. **Train your agent** (a few seconds), from the repository root
   ```bash
   python3 -m 04_qlearning.standalone.train_qlearning
   ```

3. **Play against the agent**
   ```bash
   python3 -m 04_qlearning.standalone.ttt_qlearning
   ```

4. **Integrate with OOP**
   ```bash
   python3 -m 04_qlearning.oop_integration.main
   ```

**Expected results** (canonical self-play, 20,000 games):
- Never loses against Minimax (always draws)
- Wins ~93% and loses ~0% against a random opponent

## 🎮 Quick Gameplay

Just want to play? Choose your level:

```bash
# Easy - Random opponent
python3 03_oop/main.py  # Option 1

# Impossible - Perfect Minimax
python3 03_oop/main.py  # Option 2

# Very hard - Trained agent (Q-Learning), from the repository root
python3 -m 04_qlearning.standalone.ttt_qlearning

```

## 📊 Approach Comparison

| Aspect | Basic | Minimax | Q-Learning |
|---------|--------|---------|------------|
| **Complexity** | Low | Medium | High |
| **Performance** | Poor (~50%) | Optimal | Near-optimal after training (never lost to Minimax in evaluation) |
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
- `pandas`, `seaborn` - Hyperparameter search tables and heatmap

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
- ✅ Agent training (random opponent, Minimax, self-play)
- ✅ Performance evaluation
- ✅ Hyperparameter search


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
- [ ] Use board symmetries to shrink the Q-table (exercise in notebook 05)
- [ ] Curriculum: random opponent first, then self-play
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

