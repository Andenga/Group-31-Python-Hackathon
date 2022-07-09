#Importing the relevant module
from datetime import date

#Getting today's date and storing it in a variable 'date'
date = date.today()
print("Date:", date)

#Using today's date to get the name on the day of the week written in short form with the first letter capitalized.
day = date.strftime('%a')
print("Day:", day)

#We use the weekday() method to get the name of the day of the week
#x is a variable used to store the week no from 0 to 6 representing Monday to Friday
x = date.today().weekday()

#We use an if elif else statement to determine today's fare
if x < 5:#0-4 is Mon to Fri
    print ("Fare:", 100)
elif x == 5: #5 Sat
    print ("Fare:", 60)
else:  #6 Sun
    print ("Fare:", 80)


