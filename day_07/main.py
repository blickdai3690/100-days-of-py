import random

word_list = ["aardvark", "baboon", "camel"]
choice = random.choice(word_list)
print(choice)

placeholder = ""
for c in choice:
    placeholder += "_"
print(placeholder)

game_over = False 
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter ").lower()

    display = ""

    for letter in choice:
        if guess in choice:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    
    print(display)

    if guess not in choice:
        game_over = True
        print("You lose")

    if "_" not in display:
        game_over = True
        print("You win.")

