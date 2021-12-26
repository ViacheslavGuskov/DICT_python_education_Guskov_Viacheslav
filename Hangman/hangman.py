import random

print("HANGMAN")
list_word = ["python", "java", "javascript", "php"]
win_word = random.choice(list_word)
word_progress = []
for ii in range(len(win_word)):
    word_progress.append("-")
word_step = 8
while True:
    print("".join(word_progress))
    symbola = input("Input a letter: > ")
    if symbola not in win_word:
        print("That letter doesn't appear in the word")
        continue
    for ii in range(0, len(win_word)):
        if symbola == win_word[ii]:
            word_progress[ii] = symbola
    word_step -= 1
    if word_step == 0:
        print("Thanks for playing!\nWe'll see how well you did in the next stage")
        break