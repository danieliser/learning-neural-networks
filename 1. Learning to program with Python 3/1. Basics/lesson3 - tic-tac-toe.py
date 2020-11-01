# tic-tac-toe
import os
import sys

# Linux commands to clear the terminal.
if sys.platform.startswith('linux'):
    os.system('clear')

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

print("   a  b  c")

for count, row in enumerate(game):
    print(count, row)