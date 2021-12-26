import random

print("HANGMAN")
list_word = ["python", "java", "javascript", "php"]
win_word = random.choice(list_word)
text = "Guess the word "+win_word[0:3]+("-"*(len(win_word)-3))+": > "
word = input(text)
if word == win_word:
    print("You survived!")
else:
    print("You lost!")