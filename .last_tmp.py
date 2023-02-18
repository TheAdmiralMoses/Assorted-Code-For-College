# Requirements:
# Ask the user for their grade percentage, 
# write a series of if-elif-else statements
# to print out the appropriate letter grade.
# (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

import math
grade = int(input("What is your grade %? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
    
print(f"Your letter grade is {letter}.")

# Assume that you must have at least a 70 to pass the class.
# After determining the letter grade and printing it out.
# Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them.
# If not, display a different message to encourage them for next time.

if grade >= 70:
    print ("You passed the class, good job!")
else:
    print ("You didn't pass this time, try again and work hard!")
    	
# Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block, 
# instead create a new variable called letter and then in each block, set this variable to the appropriate value. 
# Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.