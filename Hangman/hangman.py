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
    if "-" not in word_progress:
        print("You guessed the word!\nYou survived!")
        break
    if word_step == 0:
        print("You lost!")
        break
    symbola = input("Input a letter: > ")
    if symbola not in win_word:
        word_step -= 1
        print("That letter doesn't appear in the word")
        continue
    if symbola in word_progress:
        word_step -= 1
        print("No improvements")
        continue
    for ii in range(0, len(win_word)):
        if symbola == win_word[ii]:
            word_progress[ii] = symbola