print("Welcome to the tip calculator!")
sum = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
calc = (sum + (sum * (tip / 100))) / people
print(f"Each person should pay: ${calc}")