import random
cheatmode = input("Turn On Cheat mode? [y/n]: ")


n = random.randint(0, 20)
print("Guess the Number!")
if cheatmode == "y":
    print("The number is: ", n)
inp = int(input("Enter your guess: "))

while True:
    if inp == n:
        print("Correct!")
        n = random.randint(0, 20)
        print("Guess the Number!")
        if cheatmode == "y":
            print("The number is: ", n)
        inp = int(input("Enter your guess: "))
    else:
        print("Incorrect :(")
        n = random.randint(0, 20)
        print("Guess the Number!")
        if cheatmode == "y":
            print("The number is: ", n)
        inp = int(input("Enter your guess: "))
