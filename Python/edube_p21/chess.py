from enum import Enum


Color = Enum('Color', ['EMPTY', 'ROOK', 'BLUE']) # functional syntax
board = []

for i in range(8):
    row = [Color.EMPTY for i in range(8)]
    board.append(row)

board[0][0] = Color.ROOK
board[0][7] = Color.ROOK
board[7][0] = Color.ROOK
board[7][7] = Color.ROOK

print(board)