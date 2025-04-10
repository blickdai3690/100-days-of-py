print("Welcome to Treasure Island. Your mission is to find the treasure")
q1 = input("left or right? ")
if q1 == "right" or q1 != "left":
    print("Fall into a hole. Game Over.")
else:
    q2 = input("swim or wait? ")
    if q2 == "swim" or q2 != "wait":
        print("Attacked by trout. Game Over.")
    else:
        q3 = input("which door? red, blue or yellow? ")
        if q3 == "blue" or q3 != "yellow":
            print("Eaten by beasts. Game Over.")
        elif q3 == "red":
            print("Burned by fire. Game Over.") 
        else:
            print("You win!") 