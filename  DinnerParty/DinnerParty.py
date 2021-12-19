import random

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

# Этап 2. Разделение счёта меж участниками вечеринки
print("Enter the total amount:")
total_counts = int(input("> "))
one_pay = round(total_counts / count_human, 2)

for one_key in dict_human.keys():
    dict_human[one_key] = one_pay

# Этап 3. "Who is lucky?"
print("""Do you want to use the "Who is lucky?" feature? Write Yes/No:""")
user_lucky_answer = input("> ")
if user_lucky_answer == "Yes":
    user_lucky = random.choice(list(dict_human.keys()))
    print(user_lucky + " is the lucky one!")
if user_lucky_answer == "No":
    print("No one is going to be lucky.")

print(dict_human)