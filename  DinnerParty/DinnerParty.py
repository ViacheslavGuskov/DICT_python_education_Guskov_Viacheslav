# Этап 1. Добавление участников вечеринки
print("Enter the number of friends joining (including you):")
count_human = int(input("> "))
if count_human <= 0:
    print("No one is joining for the part")
    exit()

print("Enter the name of every friend (including you), each on a new line:")
dict_human = {}
for ii in range(count_human):
    dict_human[input("> ")] = 0

print(dict_human)