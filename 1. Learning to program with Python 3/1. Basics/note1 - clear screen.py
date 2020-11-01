import os
import sys

def clearScreen():
    # Linux commands to clear the terminal.
    if sys.platform.startswith('linux'):
        os.system('clear')
