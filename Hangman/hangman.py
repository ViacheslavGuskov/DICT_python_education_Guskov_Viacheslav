import random

print("HANGMAN")
list_word = ["python", "java", "javascript", "php"]
win_word = random.choice(list_word)
success_symbol = list("qwertyuiopasdfghjklzxcvbnm")
input_symbol = []
word_progress = []
for ii in range(len(win_word)):
    word_progress.append("-")
word_step = 8
while True:
    print("".join(word_progress))
    if "-" not in word_progress:
        print("You guessed the word!\nYou survived!")
        break
    if word_step == 0:
        print("You lost!")
        break
    symbola = input("Input a letter: > ")
    if len(symbola) != 1:
        print("You should input a single letter")
        continue
    if symbola not in success_symbol:
        print("Please enter a lowercase English letter")
        continue
    if symbola in input_symbol:
        print("You've already guessed this letter")
        continue
    input_symbol.append(symbola)
    if symbola not in win_word:
        word_step -= 1
        print("That letter doesn't appear in the word")
        continue
    for ii in range(0, len(win_word)):
        if symbola == win_word[ii]:
            word_progress[ii] = symbola