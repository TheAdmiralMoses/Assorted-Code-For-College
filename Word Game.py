import time
import math
print ("Welcome to my word guessing game, type a word and if you match a letter where it goes it will appear in uppercase, if not it will appear in lowercase.")
time.sleep(3)
TestWord = ""
Hint = ['_','_','_','_','_','_','_','_']
Guesses = int(0)
while TestWord != "Macaroni":
    TestWord = input("Input a word to guess! ")
    Hint = " ".join(Hint)
    print (f"Hint: {Hint}")
    list(Hint)
    Hint.replace(" ", "")
    Guesses = Guesses + 1
print ("Congrats, you win!\n")
if Guesses <2:
    print (f"You made {Guesses} guess.")
else:
    print (f"You made {Guesses} guesses.")
