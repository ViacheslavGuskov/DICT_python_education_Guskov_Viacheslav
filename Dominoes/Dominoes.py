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

double_computer_pieces = [-1]
for one_computer_piece in computer_pieces:
    if one_computer_piece[0] == one_computer_piece[1]:
        double_computer_pieces.append(one_computer_piece[0])
double_player_pieces = [-1]
for one_player_piece in player_pieces:
    if one_player_piece[0] == one_player_piece[1]:
        double_player_pieces.append(one_player_piece[0])

if max(double_computer_pieces) > max(double_player_pieces):
    status = "player"
    domino_snake.append([max(double_computer_pieces), max(double_computer_pieces)])
    computer_pieces.remove([max(double_computer_pieces), max(double_computer_pieces)])
if max(double_computer_pieces) < max(double_player_pieces):
    status = "computer"
    domino_snake.append([max(double_player_pieces), max(double_player_pieces)])
    player_pieces.remove([max(double_player_pieces), max(double_player_pieces)])

while True:
    print("=" * 70)
    print("Stock size: " + str(len(stock_pieces)))
    print("Computer pieces: " + str(len(computer_pieces)))
    if len(domino_snake) > 6:
        domino_snake_text = "\n" + str(domino_snake[0]) + str(domino_snake[1]) + str(domino_snake[2]) +\
        "..." + str(domino_snake[-3]) + str(domino_snake[-2]) + str(domino_snake[-1])
    else:
        domino_snake_text = "\n"
        for domino_snake_one in domino_snake:
            domino_snake_text += str(domino_snake_one)
    print(domino_snake_text)
    print("\nYour pieces: ")
    count = 1
    for player_piece_one in player_pieces:
        print(str(count)+":"+str(player_piece_one))
        count += 1
    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        break
    if len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        break
    if domino_snake[0][0] == domino_snake[-1][1]:
        count = 0
        for one_domino_snake in domino_snake:
            if one_domino_snake[0] == domino_snake[0][0] and one_domino_snake[1] == domino_snake[0][0]:
                count += 2
            elif one_domino_snake[0] == domino_snake[0][0] or one_domino_snake[1] == domino_snake[0][0]:
                count += 1
            if count == 8:
                print("Status: The game is over. It's a draw!")
                break
    if status == "computer":
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
        input_res = input("")
        place_piece = random.choice(range(-(len(computer_pieces)), len(computer_pieces)))
        if place_piece == 0:
            computer_get = random.choice(stock_pieces)
            stock_pieces.remove(computer_get)
            computer_pieces.append(computer_get)
        elif place_piece > 0:
            domino_snake.append(computer_pieces[place_piece-1])
            computer_pieces.remove(computer_pieces[place_piece-1])
        elif place_piece < 0:
            domino_snake.insert(0, computer_pieces[-place_piece-1])
            computer_pieces.remove(computer_pieces[-place_piece-1])
        status = "player"
    elif status == "player":
        print("\nStatus: It's your turn to make a move. Enter your command.")
        try:
            input_res = int(input(""))
        except:
            print("Invalid input. Please try again.")
            continue
        if input_res > len(player_pieces) or input_res < -(len(player_pieces)):
            print("Invalid input. Please try again.")
            continue
        if input_res == 0:
            player_get = random.choice(stock_pieces)
            stock_pieces.remove(player_get)
            player_pieces.append(player_get)
        elif input_res > 0:
            domino_snake.append(player_pieces[input_res-1])
            player_pieces.remove(player_pieces[input_res-1])
        elif input_res < 0:
            domino_snake.insert(0, player_pieces[-input_res-1])
            player_pieces.remove(player_pieces[-input_res-1])
        status = "computer"