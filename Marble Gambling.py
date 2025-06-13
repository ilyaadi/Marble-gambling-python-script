import random

marbles = [ ]
blackMarbles = 0
whiteMarbles = 0
redMarbles = 0
numberOfMarbles = 0

def inputNumberOfMarbles():
    while True:
        print("")
        numberOfMarbles = input("Choose number of marbles you want in the bag: ")
        if numberOfMarbles.isnumeric() and int(numberOfMarbles) > 2:
            return int(numberOfMarbles)
        print("Please enter a valid number.")

def marbleArrangement(numberOfMarbles, blackMarbles, redMarbles, whiteMarbles):
    global blackMarblesMultiplier, redMarblesMultiplier, whiteMarblesMultiplier
    for i in range(int(numberOfMarbles)):
        marble = random.randint(1,3)
        # print(marble)
        if marble == 1:
            blackMarbles += 1
            marbles.append("black")
        elif marble == 2:
            whiteMarbles +=1
            marbles.append("white")
        else:
            redMarbles += 1 
            marbles.append("red")

    blackMarblesMultiplier = ((numberOfMarbles - blackMarbles)/numberOfMarbles)+1
    whiteMarblesMultiplier = ((numberOfMarbles - whiteMarbles)/numberOfMarbles)+1
    redMarblesMultiplier = ((numberOfMarbles - redMarbles)/numberOfMarbles)+1

    print(f"\nThere are {blackMarbles} black marbles, {whiteMarbles} white marbles and {redMarbles} red marbles\n")
    print(f"black marble multiplier = {blackMarblesMultiplier}")
    print(f"white marble multiplier = {whiteMarblesMultiplier}")
    print(f"red marble multiplier = {redMarblesMultiplier}\n")

def inputMarbleColor():
    while True:
        chooseColor = input("Choose the color of the marble you would like to place your bet on, 'black', 'white; or 'red': \n")
        if chooseColor in ["red", "white", "black"]:
            return chooseColor
        else:
            ("Invalid color.") 
    
def marbleGame(chooseColor, moneyToGamble, blackMarblesMultiplier, whiteMarblesMultiplier, redMarblesMultiplier, marbleIndex):
    # print(blackMarblesMultiplier, redMarblesMultiplier, whiteMarblesMultiplier)
    if marbles[marbleIndex] == chooseColor:
        print("You Won")
        if chooseColor == "red":
            print(f"Balance is {moneyToGamble * redMarblesMultiplier}")
        elif chooseColor == "black":
            print(f"Balance is {moneyToGamble * blackMarblesMultiplier}")
        else:
            print(f"Balance is {moneyToGamble * whiteMarblesMultiplier}")
    else:
        print("\nYou Lost\n")
    print(f"The bag of marbles was in the order: \n {marbles}")
    
def inputMoney():
    while True:
        moneyToGamble = input("\nHow much money would you like to gamble: ")
        if moneyToGamble.isnumeric() and int(moneyToGamble) > 0:
            return int(moneyToGamble)
        print("Please enter a valid number.")

def inputMarbleIndex(numberOfMarbles):
    while True:
        marbleIndex = input(f"Choose the marble index, make sure its within the range of 1 - {numberOfMarbles}: ")
        if marbleIndex.isnumeric() and int(marbleIndex) <= (numberOfMarbles):
            return (int(marbleIndex) - 1)
        print("Please enter a valid number.")

def repeat():
    while True:
        rep = input("\nDo you wanna continue, choose 'yes' or 'no': ")
        if rep in ["yes", "no"]:
            break
        else:
            print("Invalid input, please enter 'yes' or 'no': ")
    if rep == "yes":
        main() 
    else:
        print("Bye!")

def main():
    numberOfMarbles = inputNumberOfMarbles()
    moneyToGamble = inputMoney()
    marbleArrangement(numberOfMarbles, blackMarbles, redMarbles, whiteMarbles)
    chooseColor = inputMarbleColor()
    marbleIndex = inputMarbleIndex(numberOfMarbles)
    marbleGame(chooseColor, moneyToGamble, blackMarblesMultiplier, whiteMarblesMultiplier, redMarblesMultiplier, marbleIndex)
    repeat()

main()