# Этап 1. Сетка.
print("X O X\n""O X O\n""X X O")
# Этап 2. Игровое поле
def tictactoeboard():
    print('Enter cells:')
    tttb = list(input())
    print('---------')
    print('| ' + tttb[0] + ' ' + tttb[1] + ' ' + tttb[2] + ' |')
    print('| ' + tttb[3] + ' ' + tttb[4] + ' ' + tttb[5] + ' |')
    print('| ' + tttb[6] + ' ' + tttb[7] + ' ' + tttb[8] + ' |')
    print('---------')
tictactoeboard() 