# tic-tac-toe
from itertools import cycle
import os
import sys


def clear_screen():
    # Linux commands to clear the terminal.
    if sys.platform.startswith('linux'):
        os.system('clear')


def win(current_game):
    def all_same(L):
        if L[0] != 0 and L.count(L[0]) == len(L):
            return True
        else:
            return False

    # Horizontal
    for row in current_game:
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (-)!")
            return True

    # Diagonal
    diags = []
    for idx in range(len(game)):
        diags.append(game[idx][idx])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diaganal (\\)!")
        return True

    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} is the winner diaganal (/)!")
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            # print(row[0])
            check.append(row[0])

        if all_same(check):
            print(f"Player {row[0]} is the winner vertical (|)!")
            return True

    return False


def game_board(game_map, player: int = 0, row: int = 0, column: int = 0, just_display: bool = False):
    try:
        clear_screen()
        if game_map[row][column] != 0:
            print("This position is occupied! Choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(game_size)]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False


game_size = int(input("Game grid size? ex. 3: "))
game = []
play = True
players = range(int(input("Number of players? "))+1)[1:]
max_turns = game_size * game_size
print(max_turns)

def new_game():
    game = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        game.append(row)

    return game


while play:
    game = new_game()
    turn = 0

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_cycle = cycle(players)
    while not game_won:
        current_player = next(player_cycle)
        print(f"Current Player: {current_player}")
        played = False
        turn = turn + 1

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
                game, _ = game_board(new_game(), just_display=True)
            else:
                print("Bye")
                play = False
        elif turn >= max_turns:
            print("Nobody wins")
            again = input("The game is over, would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("restarting")
                game, _ = game_board(new_game(), just_display=True)
            else:
                print("Bye")
                play = False
