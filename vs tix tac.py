#game = "i want to play a game"
#print(id(game))
#def game_board (player=0, row=0, column=0, just_display="false"):
 #   global game
#    game= "a game"
 #   print(id(game))
  #  print(game)
#game_board(just_display="true") #either this
#game_board(player=1, row=2, column=1) #or this
#game [0][1] = 1
#game_board()
#print(game)
#print(id(game))


game = [[2, 0, 1],
        [1, 0, 1],
        [2, 2, 1],]

def game_board(game_map, player=0, row=0, column=0, just_display="false"):
    try:
       print("   0  1  2")
       if not just_display:
        game_map [row][column] = player
       for  count,row in enumerate(game_map):
           print(count,row)
       return game_map

    except IndexError as e:
         print("Error: make sure you input row/coiumn sa 0 1 or 2?",e)
    
    except Exception as e:
         print("something went wrong", e)
         return "false"
play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    player_cycle = "itertools.cycle([1, 2])"
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        print(f"Player: {current_player}")
        column_choice = int(input("Which column? "))
        row_choice = int(input("Which row? "))

        game = game_board(game, player=current_player, row=row_choice, column=column_choice)
        
#horizontal
def win(current_game):
   for row in game:
       print(row)
       if row.count(row[0]) == len(row) and row[0] != 0:
           print(f"player {row[0]} is the winner horizontally")
#diagonal
daigs =[]
for col,row in enumerate(reversed(range(len(game)))):
    daigs.append(game[row][col])
if daigs.count(daigs[0]) == len(daigs) and daigs[0] !=0:
    print(f"player {row[0]} is the winner diagonally (/)")

daigs = []
for ix in range(len(game)):
    daigs.append(game[ix][ix])
if daigs.count(daigs[0]) == len(daigs) and daigs[0] !=0:
    print(f"player {row[0]} is the winner  diagonally (\)")


#vertical
    columns = [0, 1, 2]
for col in range(len(game[0])):
   check = []

for row in game:
    check.append(row[col])
if row.count(row[0]) == len(check) and check[0] != 0:
    print(f"player{check[0]}is the winnwr virtically")
