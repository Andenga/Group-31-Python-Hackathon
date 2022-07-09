#We begin by importing the relevant module.
#We need datetime library to print when the door was last opened or closed.
import datetime 

#We use the timedelta() function to calculate the difference in datetime
Date = datetime.datetime.today() - datetime.timedelta()
#We store our password in a variable named password 
#Our password is set to admin
password = "admin"
#We then declare the following variables
open = "open"
close = "close"
quit = "quit"

#We ask the user to input the password
#Password is admin
user_input = raw_input("Enter password: ")

#We use a while loop that only breaks when the user inputs the right password otherwise it runs an error message and reruns again
#We then use an if elif statement to ask the user to enter a command then we determine the output
while user_input != password:
  print("Wrong password,Please try again.")
  user_input = input("Enter password: ")
else:
    print("Proceed!")
    command = input("Enter a command")
    if command == open:
        print("The door is now open")
        print("Door last open at: ", Date)
    elif command == close:
        print("The door is now locked")
        print("Door last looked at: ", Date)
    elif command == quit:
        print("The process has been terminated")
    elif command != open or command != close or command!= quit:
           print("Invalid input")
    
    command0 = input("Enter another command for the door")
    if command0 == open:
        if command == command0:
            print("The door is already open")
        else:    
            print("The door is now open")
            print("Door last open at: ", Date)
    elif command0 == close:
        if command == command:
            print("The door is alrerady locked")
        else:
            print("The door is looked")
            print("Door last looked at: ", Date)
    elif command0 == quit:
        print("The process has been terminated")
       
    elif command0 != open or command0 != close or command0 != quit:
            print("Invalid input")
