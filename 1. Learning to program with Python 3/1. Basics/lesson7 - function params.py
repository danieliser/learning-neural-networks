# tic-tac-toe
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]

def game_board(player: int=0, row: int=0, column: int=0, just_display: bool=False):
    
    print("   a  b  c")

    if not just_display:
        game[row][column] = player
    for count, row in enumerate(game):
        print(count, row)

game_board(just_display=True)

game_board(player=1, row=1, column=1)
