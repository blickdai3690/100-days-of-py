import random

lst = ["rock", "paper", "scissors"]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
your_choice = lst[choice]
comp_choice = random.choice(lst)
msg = "You win!"

if your_choice == "rock" and comp_choice == "scissors":
    print(msg)
elif your_choice == "scissors" and comp_choice == "paper":
    print(msg)
elif your_choice == "paper" and comp_choice == "rock":
    print(msg)
else:
    print("You lose!")