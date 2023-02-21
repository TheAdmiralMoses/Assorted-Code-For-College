import time
import math
import random
def start_game():
    KeyWordList = ["moroni","alma","nephi"]
    print ("Welcome to my word guessing game, type a word and if you match a letter where it goes it will appear in uppercase, if not it will appear in lowercase.")
    TestWord = ""
    KeyWord = random.choice(KeyWordList)
    Guesses = int(0)
    Hint = ""
    for letter in KeyWord:
        Hint += " _"
    while TestWord != KeyWord:
        print (f"Your hint is:{Hint}")
        TestWord = input("Input a word to guess! ")
        TestWord = TestWord.lower()
        if len(TestWord) < len(KeyWord):
            print ("That word is too short")
        elif len(TestWord) > len(KeyWord):
            print ("That word is too long")
        else:
            Hint = ""
            for i, letter in enumerate(TestWord):
                for i2, letter2 in enumerate(KeyWord):
                    if i == i2 and letter ==  letter2:
                        letter = letter.upper()
                        Hint += f" {letter}"
                        break
                else:
                    if letter in KeyWord:
                        Hint += f" {letter}"
                    else:
                        Hint +=" _"
        Guesses = Guesses + 1
    print ("Congrats, you win!\n")
    if Guesses <2:
        print (f"You made {Guesses} guess.")
    else:
        print (f"You made {Guesses} guesses.")
    while True:
        replay = input("Play again? Type Y or N")
        replay = replay.lower()
        if replay == "y":
            start_game()
        elif replay == "n"
            break
        else:
            print("That is not an option, try again")
if __name__ == "__main__":
    start_game()
