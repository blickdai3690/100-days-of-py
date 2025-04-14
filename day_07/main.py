import random

word_list = ["aardvark", "baboon", "camel"]
choice = random.choice(word_list)
print(choice)

guess = input("Guess a letter ").lower()

for letter in choice:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")