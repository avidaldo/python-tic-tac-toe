# The Minimax Algorithm: A Pedagogical Guide

## Table of Contents
1. [What is Minimax?](#what-is-minimax)
2. [Historical Relevance and AI](#historical-relevance-and-ai)
3. [How Minimax Works](#how-minimax-works)
4. [Step-by-Step Example](#step-by-step-example)
5. [Implementation Analysis](#implementation-analysis)
6. [Complexity and Optimizations](#complexity-and-optimizations)

---

## What is Minimax?

**Minimax** is a decision-making algorithm used in game theory and artificial intelligence for choosing the optimal move in two-player, zero-sum games with perfect information. The name "minimax" comes from its strategy:

- **Maximize** your own score
- **Minimize** your opponent's score

In games like Tic-Tac-Toe, Chess, or Checkers, minimax assumes both players play optimally. The algorithm explores all possible future game states and chooses the move that leads to the best guaranteed outcome.

### Key Characteristics

- **Adversarial search**: Assumes an intelligent opponent
- **Recursive**: Explores the game tree by calling itself
- **Backtracking**: Evaluates positions by looking ahead to terminal states
- **Zero-sum**: One player's gain is the other's loss

---

## Historical Relevance and AI

### Origins in Game Theory (1920s-1940s)

The minimax theorem was first proven by **John von Neumann** in 1928, laying the foundation for game theory. This mathematical framework provided a rigorous way to analyze strategic decision-making in competitive scenarios.

Von Neumann's work on minimax extended beyond games to economics, military strategy, and eventually artificial intelligence. His 1944 book (with Oskar Morgenstern), *Theory of Games and Economic Behavior*, revolutionized how we think about rational decision-making.

### The Dawn of AI (1950s-1960s)

Minimax became one of the first algorithms implemented in early AI programs:

- **1950**: Claude Shannon published "Programming a Computer for Playing Chess," describing how minimax could be applied to chess
- **1951**: Dietrich Prinz wrote the first chess-playing program using minimax principles
- **1956**: The Dartmouth Conference (birth of AI as a field) featured discussions on game-playing programs
- **1959**: Arthur Samuel's checkers program used minimax with learning, eventually beating human champions

### Why Minimax Matters in AI History

1. **Proof of Concept**: Early AI researchers used games to demonstrate that machines could exhibit "intelligent" behavior
2. **Search and Decision-Making**: Minimax introduced fundamental concepts like search trees, evaluation functions, and lookahead
3. **Adversarial Reasoning**: Modeling an opponent's optimal play became a template for multi-agent systems
4. **Benchmarking Intelligence**: Games like Chess became standard tests for AI capabilities

### Modern Legacy

While modern game-playing AI (like AlphaGo and chess engines) uses more sophisticated techniques, minimax remains:

- A pedagogical cornerstone for teaching AI and algorithms
- The foundation for advanced techniques like **alpha-beta pruning**, **Monte Carlo Tree Search**
- Relevant in domains beyond games: cybersecurity, economics, and automated negotiation

---

## How Minimax Works

### The Game Tree Concept

Minimax visualizes the game as a tree:

- **Root node**: Current game state
- **Child nodes**: Possible next states after each legal move
- **Leaf nodes**: Terminal states (win, loss, or draw)

### The Two Players

The algorithm alternates between two perspectives:

1. **Maximizing Player** (usually the AI agent): Tries to maximize the score
2. **Minimizing Player** (usually the opponent): Tries to minimize the score

### The Recursive Process

```
function minimax(state, is_maximizing):
    if state is terminal:
        return score of state

    if is_maximizing:
        best_score = -infinity
        for each possible move:
            make the move
            score = minimax(new_state, false)
            undo the move
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = +infinity
        for each possible move:
            make the move
            score = minimax(new_state, true)
            undo the move
            best_score = min(best_score, score)
        return best_score
```

### Scoring Terminal States

In Tic-Tac-Toe (as implemented in this repository):
- **AI wins**: +1
- **Human wins**: -1
- **Draw**: 0

---

## Step-by-Step Example

Let's examine a simplified Tic-Tac-Toe endgame where the AI (X) is about to move:

```
Current Board:
 X | O | X
-----------
 O | X | 6
-----------
 7 | 8 | O

Available moves for X: [6, 7, 8]
```

### Step 1: Explore Move to Cell 6

```
 X | O | X
-----------
 O | X | X
-----------
 7 | 8 | O
```

- This is a terminal state: X wins!
- Return score: **+1**

### Step 2: Explore Move to Cell 7

```
 X | O | X
-----------
 O | X | 6
-----------
 X | 8 | O
```

- Not terminal, so O (minimizing) must move
- O can move to 6 or 8

**O moves to 6:**
```
 X | O | X
-----------
 O | X | O
-----------
 X | 8 | O
```
- O wins! Score: **-1**

**O moves to 8:**
```
 X | O | X
-----------
 O | X | 6
-----------
 X | O | O
```
- O wins! Score: **-1**

- Minimizing player (O) chooses min(-1, -1) = **-1**
- Return score for move 7: **-1**

### Step 3: Explore Move to Cell 8

Following similar logic, this also leads to a loss or draw.

### Step 4: Decision

Minimax compares all explored moves:
- Cell 6: **+1** (WIN)
- Cell 7: **-1** (LOSS)
- Cell 8: **-1** (LOSS)

**Maximizing player chooses move 6** because max(+1, -1, -1) = +1

---

## Implementation Analysis

This repository contains three minimax implementations. Let's analyze them:

### Implementation 1: [ttt_v13a_minimax.py](ttt_v13a_minimax.py)

**Lines 20-43**: The `minimax()` function returns only the score.

```python
def minimax(board, is_maximizing):
    if check_winner(board) == AI:
        return 1
    if check_winner(board) == HUMAN:
        return -1
    if is_board_completed(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for cell in list_of_free_cells(board):
            board[cell] = AI
            score = minimax(board, False)
            board[cell] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in list_of_free_cells(board):
            board[cell] = HUMAN
            score = minimax(board, True)
            board[cell] = None
            best_score = min(score, best_score)
        return best_score
```

**Lines 47-59**: A separate `minimax_move()` function finds the best move.

**Characteristics**:
- Cleaner separation: evaluation vs. move selection
- Requires re-exploration for move selection
- Easier to understand for beginners

### Implementation 2: [ttt_v13b_minimax.py](ttt_v13b_minimax.py)

**Lines 19-51**: The `minimax()` function returns *both* score and move as a tuple.

```python
def minimax(board, is_maximizing) -> tuple:
    if check_winner(board) == AI:
        return 1, None
    if check_winner(board) == HUMAN:
        return -1, None
    if is_board_completed(board):
        return 0, None

    if is_maximizing:
        best_score = float("-inf")
        best_move = None
        for cell in list_of_free_cells(board):
            board[cell] = AI
            score, _ = minimax(board, False)
            board[cell] = None
            if score > best_score:
                best_score = score
                best_move = cell
        return best_score, best_move
    # ... (similar for minimizing)
```

**Characteristics**:
- More efficient: finds best move in one pass
- Directly usable: `_, best_move = minimax(board, True)`
- Slightly more complex to understand

### Implementation 3: [ttt_v21_oop/player.py](ttt_v21_oop/player.py)

**Lines 65-101**: Object-oriented implementation in `MinimaxMachinePlayer` class.

```python
class MinimaxMachinePlayer(MachinePlayer):
    def minimax(self, board, is_maximizing: bool):
        winner = board.check_winner()
        if winner == self.symbol:
            return None, 1
        elif winner is not None:
            return None, -1
        elif board.is_board_full():
            return None, 0

        best_score = float('-inf') if is_maximizing else float('inf')
        best_move = None

        for cell in board.get_free_cells():
            original_value = board[cell]
            board[cell] = self.symbol if is_maximizing else Symbol.HUMAN
            _, score = self.minimax(board, not is_maximizing)
            board[cell] = original_value

            if is_maximizing:
                if score > best_score:
                    best_score = score
                    best_move = cell
            else:
                if score < best_score:
                    best_score = score
                    best_move = cell

        return best_move, best_score
```

**Characteristics**:
- Encapsulation: minimax is a method of the player
- Flexible: `self.symbol` makes it reusable for either player
- Production-ready: better architecture for larger projects

---

## Complexity and Optimizations

### Time Complexity

For Tic-Tac-Toe:
- **Worst case**: O(9!) = 362,880 states
- **Average case**: Much less due to terminal states and symmetry
- **First move**: Evaluates ~150,000 positions

For more complex games like Chess:
- **Branching factor**: ~35 moves per position
- **Depth 10**: 35^10 ≈ 2.8 quadrillion positions

### Space Complexity

- **Recursion depth**: O(d) where d is maximum depth
- In Tic-Tac-Toe: d = 9 (maximum moves)

### Common Optimizations

1. **Alpha-Beta Pruning**
   - Prunes branches that cannot affect the final decision
   - Reduces complexity to O(b^(d/2)) in best case
   - Mentioned in comments at lines 9-10 of both minimax files

2. **Depth-Limited Search**
   - Only search to a certain depth
   - Use heuristic evaluation for non-terminal positions
   - Essential for games like Chess

3. **Move Ordering**
   - Evaluate likely good moves first
   - Improves alpha-beta efficiency

4. **Transposition Tables**
   - Cache previously evaluated positions
   - Avoid re-computing identical states

5. **Iterative Deepening**
   - Search to depth 1, then 2, then 3, etc.
   - Combines benefits of breadth-first and depth-first search

---

## Conclusion

Minimax represents a milestone in AI history: the idea that machines can reason about adversarial situations by simulating all possibilities. While modern game-playing AI has moved beyond pure minimax, understanding this algorithm is essential for:

- Grasping fundamental AI concepts (search, evaluation, decision trees)
- Appreciating the evolution from rule-based to learning-based AI
- Building intuition for multi-agent and adversarial systems

The three implementations in this repository showcase different approaches:
- **v13a**: Pedagogical clarity
- **v13b**: Efficiency through tuples
- **v21_oop**: Production-ready architecture

Each demonstrates that even a simple algorithm can be expressed in multiple ways, each with trade-offs in clarity, efficiency, and maintainability.

---

## Further Information

- Video: [Programación recursiva en python](https://www.youtube.com/watch?v=cgg1ACU49aQ)
- Video: [Minimax en el tres en raya](https://www.youtube.com/watch?v=SLgZhpDsrfc)
