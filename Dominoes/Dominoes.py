import random
while True:
    stock_pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],\
        [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]
    computer_pieces = []
    player_pieces = []
    domino_snake = []
    status = "0"
    for aa in range(7):
        computer_get = random.choice(stock_pieces)
        stock_pieces.remove(computer_get)
        computer_pieces.append(computer_get)
        player_get = random.choice(stock_pieces)
        stock_pieces.remove(player_get)
        player_pieces.append(player_get)
    if [0, 0] in stock_pieces and [1, 1] in stock_pieces and [2, 2] in stock_pieces and [3, 3] in stock_pieces and [4, 4] in stock_pieces and [5, 5] in stock_pieces and [6, 6] in stock_pieces:
        continue
    else:
        break

double_computer_pieces = [-2]
for one_computer_piece in computer_pieces:
    if one_computer_piece[0] == one_computer_piece[1]:
        double_computer_pieces.append(one_computer_piece[0] * 2)
double_player_pieces = [-2]
for one_player_piece in player_pieces:
    if one_player_piece[0] == one_player_piece[1]:
        double_player_pieces.append(one_player_piece[0] * 2)

if max(double_computer_pieces) > max(double_player_pieces):
    status = "player"
    domino_snake.append([max(double_computer_pieces)//2, max(double_computer_pieces)//2])
    computer_pieces.remove([max(double_computer_pieces)//2, max(double_computer_pieces)//2])
if max(double_computer_pieces) < max(double_player_pieces):
    status = "computer"
    domino_snake.append([max(double_player_pieces)//2, max(double_player_pieces)//2])
    player_pieces.remove([max(double_player_pieces)//2, max(double_player_pieces)//2])

print("Stock pieces: "+str(stock_pieces))
print("Computer pieces: "+str(computer_pieces))
print("Player pieces: "+str(player_pieces))
print("Domino snake: "+str(domino_snake))
print("Status: "+str(status))