import random

word_list = ["aardvark", "baboon", "camel"]
choice = random.choice(word_list)
print(choice)

placeholder = ''
for c in choice:
    placeholder += '_'
print(placeholder)

guess = input("Guess a letter ").lower()
display = ''

for letter in choice:
    if letter == guess:
        display += letter
    else:
        display += '_'
print(display)