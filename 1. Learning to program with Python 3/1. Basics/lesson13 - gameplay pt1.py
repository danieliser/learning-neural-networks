# tic-tac-toe
from itertools import cycle


def win(current_game):
    # Horizontal
    for row in current_game:
        print(row)
        if row[0] != 0 and row.count(row[0]) == len(row):
            print(f"Player {row[0]} is the winner horizontally (-)!")

    # Diagonal
    diags = []
    for idx in range(len(game)):
        diags.append(game[idx][idx])
    if diags[0] != 0 and diags.count(diags[0]) == len(diags):
        print(f"Player {diags[0]} is the winner diaganal (\\)!")

    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if diags[0] != 0 and diags.count(diags[0]) == len(diags):
        print(f"Player {diags[0]} is the winner diaganal (/)!")
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            # print(row[0])
            check.append(row[0])

        if check[0] != 0 and check.count(check[0]) == len(check):
            print(f"Player {row[0]} is the winner vertical (|)!")


def game_board(game_map, player: int = 0, row: int = 0, column: int = 0, just_display: bool = False):
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2", e)

    except Exception as e:
        print("Something went very wrong!", e)


play = True
players = [1, 2]


while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_cycle = cycle(players)
    while not game_won:
        current_player = next(player_cycle)
        print(f"Current Player: {current_player}")
        row_choice = int(input("What row do you want to play? (0, 1, 2): "))
        column_choice = int(input("What column do you want to play? (0, 1, 2): "))
        game = game_board(game, current_player, row_choice, column_choice)
        if win(game):
            game_won = True
