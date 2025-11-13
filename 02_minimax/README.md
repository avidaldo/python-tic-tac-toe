# 02 - Minimax Algorithm

This folder contains implementations of the Minimax algorithm, which creates an unbeatable AI for Tic-Tac-Toe.

## Contents

### 📚 [MINIMAX_ALGORITHM.md](MINIMAX_ALGORITHM.md)
Complete document explaining:
- What the Minimax algorithm is
- How it works step by step
- Decision tree
- State evaluation
- Implementation in Python

### 🤖 [ttt_v13a_minimax.py](ttt_v13a_minimax.py)
**Educational Version - Recommended for Learning**

Clear and didactic implementation with separated concerns:
- `minimax()` returns only the **score** (simpler to understand)
- Separate `minimax_move()` function finds the best move
- Step-by-step recursion explained
- Each function has a single responsibility
- **Best for**: Understanding the algorithm

**Trade-off**: Evaluates the game tree twice (less efficient)

**Run:**
```bash
python3 ttt_v13a_minimax.py
```

### 🤖 [ttt_v13b_minimax.py](ttt_v13b_minimax.py)
**Optimized Version - Production Ready**

More efficient implementation with integrated approach:
- `minimax()` returns **both score and best move** (tuple)
- Evaluates the game tree only once
- More concise `minimax_move()` implementation
- Follows production best practices
- **Best for**: Real applications and performance

**Trade-off**: Slightly more complex to understand at first

**Run:**
```bash
python3 ttt_v13b_minimax.py
```

### 📊 Comparison

| Aspect | v13a (Educational) | v13b (Optimized) |
|--------|-------------------|------------------|
| **Clarity** | ⭐⭐⭐⭐⭐ Easier to learn | ⭐⭐⭐⭐ More complex |
| **Efficiency** | ⭐⭐⭐ Evaluates twice | ⭐⭐⭐⭐⭐ Evaluates once |
| **Code Length** | Longer, more verbose | Shorter, more concise |
| **Best For** | Learning & Teaching | Production & Performance |
| **Correctness** | ✅ Fully correct | ✅ Fully correct |

**Both play identically** - they produce the exact same moves and are unbeatable.

### 🔍 Technical Explanation

**Why v13a evaluates twice:**
```python
# v13a approach:
def minimax(board, is_maximizing):
    # Returns only the score
    return best_score

def minimax_move(board):
    # Must iterate and call minimax() for each possible move
    for move in possible_moves:
        score = minimax(board, False)  # Evaluates full tree
        # Compare scores to find best
```

**Why v13b is more efficient:**
```python
# v13b approach:
def minimax(board, is_maximizing):
    # Returns both score AND the move that achieves it
    return best_score, best_move

def minimax_move(board):
    # Simply extracts the move from minimax result
    _, best_move = minimax(board, True)  # Evaluates tree once
    return best_move
```

**Performance Impact:**
- For tic-tac-toe: Negligible (game tree is small)
- For larger games (Chess, Go): v13b would be significantly faster
- v13a: ~10,000 node evaluations per move
- v13b: ~5,000 node evaluations per move

## What is Minimax?

**Minimax** is a game theory algorithm that:
1. Explores all possible moves
2. Assumes the opponent plays optimally
3. Chooses the move that maximizes the guaranteed minimum gain

### Visual Example

```
        [Current State]
       /      |      \
    [M1]    [M2]    [M3]
    / | \   / | \   / | \
  ...  ...  ...  ...  ...
```

The algorithm:
- **Maximizes** on your turn (seeks best move)
- **Minimizes** on opponent's turn (assumes perfect play)

## Concepts Learned

- 🧠 **Advanced recursion**: Functions that call themselves
- 🎯 **Game algorithms**: Applied game theory
- 🌳 **Decision trees**: State exploration
- 📊 **Heuristic evaluation**: Assigning values to states
- ⚡ **Optimization**: Alpha-beta pruning (in advanced versions)


