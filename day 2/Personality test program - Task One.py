
#We ask the user to enter the number of books that he/she has purchased this month
#We use the while loop to create a loop that only breaks when the write data type has been input
#The if statement makes sure the input is a positive integer before the loop breaks.
#The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.

while True:
    try:
        no_of_books = input("Enter the number of books you have purchased this month:")
        no_of_books = int(no_of_books)
        if no_of_books < 0:  # if not a positive integer print message and ask for input again
            print("Sorry, input must be a positive integer, try again")
            continue
        break
    except ValueError:
        print("Not a valid integer. Please try again")

#We use an if elif else statement to show how the points are awarded and determine the right output.

if no_of_books == 0:
    print("points awarded: 0 points")
elif no_of_books == 1:
    print("points awarded: 6 points")
elif no_of_books == 2:
    print("points awarded: 16 points")
elif no_of_books == 3:
    print("points awarded: 32 points")
else:
    print("points awarded: 60 points")

