# Этап 1. Сетка.
print("X O X\n""O X O\n""X X O")
# Этап 2. Игровое поле
def tictactoeboard():
    tttb = list(input('Enter cells: '))
    print(tttb)
    print('---------')
    print('| ' + tttb[0] + ' ' + tttb[1] + ' ' + tttb[2] + ' |')
    print('| ' + tttb[3] + ' ' + tttb[4] + ' ' + tttb[5] + ' |')
    print('| ' + tttb[6] + ' ' + tttb[7] + ' ' + tttb[8] + ' |')
    print('---------')
    return tttb
tictactoeboard()
# Этап 3. Вводимые данные
data_list = tictactoeboard()
win_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
win_stat = [0, 0]
for one_variant in win_list:
    if data_list[one_variant[0]] == "X" and data_list[one_variant[1]] == "X" and data_list[one_variant[2]] == "X":
        win_stat[0] = 1
    if data_list[one_variant[0]] == "O" and data_list[one_variant[1]] == "O" and data_list[one_variant[2]] == "O":
        win_stat[1] = 1
count_x = 0
count_o = 0
for ii in data_list:
    if ii == "X":
        count_x += 1
    if ii == "O":
        count_o += 1
if win_stat[0] == 1 and win_stat[1] == 1:
    print("Impossible")
elif count_x - count_o > 1 or count_x - count_o  < -1:
    print("Impossible")
else:
    if win_stat[0] == 1:
        print("X wins")
    elif win_stat[1] == 1:
        print("O wins")
    else:
        if "_" not in data_list:
            print("Draw")
        elif "_" in data_list:
            print("Game not finished")
