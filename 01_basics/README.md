# 01 - Basic Implementations

This folder contains basic Tic-Tac-Toe implementations in Python, ideal for learning language fundamentals.

## Contents

### 📋 [assignment.md](assignment.md)
Original exercise assignment with game requirements.

### 📝 [ttt_v11_list_of_lists.py](ttt_v11_list_of_lists.py)
**First version: List of lists**

Implementation using a simple data structure:
```python
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
```

**Concepts learned:**
- Nested lists (matrices)
- Nested for loops
- Basic functions
- Input/output
- Conditionals

**Run:**
```bash
python3 ttt_v11_list_of_lists.py
```

### 📝 [ttt_v12_dict.py](ttt_v12_dict.py)
**Second version: Dictionary**

Implementation using a dictionary to represent the board:
```python
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
```

**Concepts learned:**
- Dictionaries in Python
- Numeric keys
- Direct position access
- Dictionary iteration

**Explanatory video:** [Tres en raya en Python desde menos uno](https://www.youtube.com/watch?v=ek0L_xk3YBk)

**Run:**
```bash
python3 ttt_v12_dict.py
```

## Approach Comparison

| Aspect | List of lists | Dictionary |
|---------|----------------|-------------|
| Access | `board[row][col]` | `board[cell]` |
| Intuitiveness | Less intuitive | More intuitive (1-9) |
| Complexity | Higher (indices 0-2) | Lower (indices 1-9) |
| Ideal for | Learning matrices | Simple games |

