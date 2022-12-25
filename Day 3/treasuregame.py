print(" Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("where would you like to go? left or right: ").lower()
if choice1== "left":
    choice2 = input("what would you like to do next? swim or wait: ").lower()
    if choice2 == "wait":
        choice3 = input("which door would you like to enter now? yellow, blue or red: ").lower()
        if choice3 == "yellow":
            print("you win!")
        elif choice3 == "blue":
            print("game over!eaten by a beast")
        elif choice3 == "red":
            print("game over!burned by fire")
        else:
            print("game over!")
    else:
        print("attacked by trout! game over")
else:
    print("game over")
    
