# tic-tac-toe
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(game_map, player: int=0, row: int=0, column: int=0, just_display: bool=False):  
    try:
        print("   a  b  c")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError as e:
        print ("Error: make sure you input row/column as 0 1 or 2", e)
    except Exception as e:
        print ("Something went very wrong!", e)

game = game_board(game, just_display=True)

game = game_board(game, player=1, row=1, column=1)
