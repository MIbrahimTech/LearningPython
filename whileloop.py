import random

#While loop example
while True:
    random_number = int(random.randint(1, 20))
    print(f"You rolled a {random_number}.")
    roll_again = input("Do you want to roll again?").lower()
    if roll_again == "y":
        continue
    if roll_again == "n":
        break