import time
import math
print ("Welcome to my word guessing game, type a word and if you match a letter where it goes it will appear in uppercase, if not it will appear in lowercase.")
time.sleep(3)
KeyWord = Macaroni
TestWord = ""
Hint = "_ _ _ _ _ _ _ _"
Guesses = int(0)
while TestWord != KeyWord:
    print (f"Hint: {Hint}")
    TestWord = input("Input a word to guess! ")
    list(TestWord)
    for letter in TestWord:
        if letter == KeyWord:
            break
        else:
            break
    Guesses = Guesses + 1
print ("Congrats, you win!\n")
if Guesses <2:
    print (f"You made {Guesses} guess.")
else:
    print (f"You made {Guesses} guesses.")
