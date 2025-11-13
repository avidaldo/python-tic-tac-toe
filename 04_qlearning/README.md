# 04 - Q-Learning (Reinforcement Learning)

This folder contains a complete implementation of **Q-Learning** applied to Tic-Tac-Toe, demonstrating how an agent can learn to play through trial and error.

## 📚 Project Structure

```
04_qlearning/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
│
├── theory/                      # 📖 Theory and educational notebooks
│   └── tictactoe_qlearning.ipynb
│
├── training/                    # 🎓 Agent training
│   ├── environment.py           # Game environment (shared module)
│   ├── q_learning_agent.py      # Agent implementation (shared module)
│   ├── train_qlearning.py       # Training script
│   ├── demo.py                  # Quick demo
│   └── q_table.pkl              # Trained Q-table (365KB)
│
├── standalone/                  # 🎮 Standalone game
│   └── ttt_qlearning.py         # CLI to play vs agent
│
└── oop_integration/             # 🔗 Integration with OOP version
    ├── README.md                # Integration guide
    ├── q_learning_player.py     # QLearningMachinePlayer
    └── main.py                  # OOP game + Q-Learning
```

## 🚀 Quick Guide

**Important:** All scripts must be run as Python modules from the project root directory (`python-tic-tac-toe/`).

### Why Run as Modules?

This project uses **relative imports** to share code between components without duplication. When you run a script as a module with `python3 -m`, Python treats the entire project as a package, allowing imports like `from ..training.q_learning_agent import QLearningAgent` to work correctly. This approach eliminates the need for manual `sys.path` manipulation and ensures consistent file paths regardless of where you run the command from.

**Module execution** means running Python code using `-m` followed by the module path (with dots instead of slashes): `python3 -m 04_qlearning.standalone.ttt_qlearning` instead of `python3 04_qlearning/standalone/ttt_qlearning.py`. This tells Python to treat `04_qlearning` as a package and resolve all relative imports correctly.

### Option 1: Use the Pre-trained Agent

```bash
# From the project root (python-tic-tac-toe/)
python3 -m 04_qlearning.standalone.ttt_qlearning
```

### Option 2: Train Your Own Agent

```bash
# 1. Install dependencies
pip install -r 04_qlearning/requirements.txt

# 2. Train (5-10 minutes, 50,000 episodes)
python3 -m 04_qlearning.training.train_qlearning

# 3. View demo
python3 -m 04_qlearning.training.demo

# 4. Play
python3 -m 04_qlearning.standalone.ttt_qlearning
```

### Option 3: Integrate with OOP Version

```bash
# From the project root
python3 -m 04_qlearning.oop_integration.main
```

## 📖 Step-by-Step Learning

### Step 1: Understand the Theory

Open the educational notebook:
```bash
jupyter notebook theory/tictactoe_qlearning.ipynb
```

**Notebook contents:**
1. What is Reinforcement Learning?
2. Q-Learning algorithm explained
3. Bellman equation step by step
4. Implementation from scratch
5. Interactive training
6. Q-values visualization
7. Play against the agent

### Step 2: Train your Agent

```bash
# From the project root
python3 -m 04_qlearning.training.train_qlearning
```

**What happens during training?**

1. **Episode 1-10,000**: High exploration (ε=1.0 → 0.01)
   - Agent tries random moves
   - Learns what works and what doesn't
   - Win rate: ~50-70%

2. **Episode 10,000-30,000**: Refinement
   - Less exploration, more exploitation
   - Q-values stabilize
   - Win rate: ~70-80%

3. **Episode 30,000-50,000**: Convergence
   - Nearly optimal strategy
   - Win rate: ~80-85%

**Expected result:**
- Win rate: 83-85% (vs random opponent)
- Loss rate: 5-7%
- Draw rate: 10-12%
- Q-table: ~12,500 entries, ~4,500 unique states

### Step 3: Analyze the Trained Agent

```bash
# From the project root
python3 -m 04_qlearning.training.demo
```

Shows:
- Q-table statistics
- 10 demonstration games
- Agent performance

### Step 4: Play Against the Agent

**Option A - Standalone:**
```bash
# From the project root
python3 -m 04_qlearning.standalone.ttt_qlearning
```

**Option B - Integrated in OOP:**
```bash
# From the project root
python3 -m 04_qlearning.oop_integration.main
```


## 🔬 Advanced Experiments

### 1. Self-Play

```python
# Train against another agent instead of random
agent2 = QLearningAgent(symbol='O', training_mode=True)
play_training_game(agent1, opponent_agent=agent2)
```

### 2. Train vs Minimax
Stronger agent → learns optimal strategy faster.

### 3. Board Symmetries
Reduce Q-table by recognizing equivalent states:
```
X| |O     O| |X     Same
-----  =  -----  =  strategy
 | |       | |      (rotation)
 | |       | |
```

### 4. Transfer Learning
Use Tic-Tac-Toe Q-table for similar games.


## 🏗️ Code Architecture

The codebase uses a **modular architecture** to eliminate duplication:

```
Core Modules (training/):
  ├─ environment.py        ← Single source of truth for game logic
  ├─ q_learning_agent.py   ← Shared Q-Learning implementation
  └─ train_qlearning.py    ← Training pipeline

Consumers:
  ├─ standalone/ttt_qlearning.py        ← Extends environment for CLI
  ├─ theory/tictactoe_qlearning.ipynb   ← Imports modules for teaching
  └─ oop_integration/                   ← Adapts for OOP architecture
```

**Benefits:**
- ✅ No code duplication between notebook and scripts
- ✅ Single source of truth for each class
- ✅ Easier maintenance and bug fixes
- ✅ Notebook focuses on explanation, not implementation

## 💡 Conclusion

You've built an RL agent from scratch that:
- Learns without being told the rules
- Improves with experience
- Plays almost optimally

**This is the foundation of:**
- AlphaGo (defeated Go champion)
- Video game agents (Dota 2, Starcraft)
- Robotics (motion control)
- Recommendation systems
