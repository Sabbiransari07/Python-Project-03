import random

target = random.randint(1, 100)

while True:
    userChoice = input(" Guess the target or Quit(Q):")
    if(userChoice == "Q"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Target found successfully")
        break
    elif(userChoice < target):
        print("your number is too small. take a bigger number....")
    else:
        print("your number is too big. take a smaller number.....")


print("---GAME OVER---")