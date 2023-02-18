import time

choice = input("Welcome to my game, it is quite simple, just type the text displayed in caps to make a decision. Try it for yourself to START the game. \n ")
while True:
    choice = choice.lower()
    if choice == "start":
        break
    else:
        choice = input("That is not an option, try again. ")
time.sleep(1)
print ("Excellent, lets begin!")
time.sleep(2)
while True:
    choice = input("\n You find yourself in the mouth of a cave, will you ENTER or LEAVE, or perhaps you will stop to eat some GRAPES? ")
    choice = choice.lower()
    if choice == "enter":
         print ("You enter the cave, its warm, quite warm, eventually you come upon a large pile of gold, but don't have the chance to count it because you fell for a dragon trap.\n")
         loop = input ("TRY AGAIN? (or type anything to end)\n")
         loop = loop.lower()
         if loop == "try again":
            continue
         else:
            break
    elif choice == "leave":
        print ("You walk away.")
        loop = input ("TRY AGAIN? (or type anything to end)\n")
        loop = loop.lower()
        if loop == "try again":
           continue
        else:
           break
    elif choice == "grapes":
        print ("You sit down at the entrance of the cave and eat some grapes as a knight passes you by to to battle with the dragon he says is in the cave, good thing you didn't enter it! He emerges later, and gives you some gold to share his riches")
        loop = input ("TRY AGAIN? (or type anything to end)\n")
        loop = loop.lower()
        if loop == "try again":
           continue
        else:
           break
    else:
        choice = input("That is not an option, try again. ")
print ("\nThe End")
