def commitment_script():
    word = "commitment"
    fav_letter = input ("What is your favorite letter? ")
    output = ""
    fav_letter = fav_letter.lower()
    for letter in word:
        if letter == fav_letter:
            print (letter.upper(), end='')
        else:
            print (letter.lower(), end='')
    print ()
def word_scrip()
    quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
    cont = "yes"
    while True:
        number = input("Write a number ")
        for i, letter in enumerate(quote):
            if (i) %int(number) == 0:
                print(letter.capitalize(), end='')
            else:
                print(letter, end='')
        print()
        cont = input("Would you like to enter another number? (yes or no)")
        if cont.lower() == "yes":
            continue
        elif cont.lower() == "no":
            print("Goodbye!")
            break
while __name__ == "__main__":
    choice = int(input("Input 1 to run the commitmnt script, input 2 to run the quote script, or input 3 to end. "))
    if choice == 1:
        commitment_script()
    elif choice == 2:
        word_script()
    elif choice == 3:
        break
    else:
        print ("That is not an option, try again.")