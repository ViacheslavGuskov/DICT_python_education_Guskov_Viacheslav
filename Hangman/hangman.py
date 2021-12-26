import random

print("HANGMAN")
list_word = ["python", "java", "javascript", "php"]
win_word = random.choice(list_word)
word = input("Guess the word: > ")
if word == win_word:
    print("You survived!")
else:
    print("You lost!")