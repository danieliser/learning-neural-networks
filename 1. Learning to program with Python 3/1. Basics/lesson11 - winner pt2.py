# tic-tac-toe
game = [[1, 1, 1],
        [0, 0, 0],
        [0, 0, 0]]

for col in range(len(game)):
    check = []

    for row in game:
        # print(row[0])
        check.append(row[0])

    if check[0] != 0 and check.count(check[0]) == len(check):
        print("Winner!")

'''
def win(current_game):
    for row in current_game:
        print(row)
        if row[0] != 0 and row.count(row[0]) == len(row):
            print("Winner!")
'''


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


'''
game = game_board(game, just_display=True)
win(game)
game = game_board(game, player=1, row=1, column=1)
'''
