
#We ask the members to input the number of fat grams they consumed in a day
#We use a while loop to create a loop that only breaks when the user inputs the right data type
#The if statement makes sure the input is a positive integer before the loop breaks.
#The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.

while True:
    try:
        fat_gram = input("Input the number of fat grams: ")
        fat_gram = int(fat_gram)
        if fat_gram < 0:
            print("Sorry, input must be a positive integer. Please try again")
            continue
        break
    except ValueError:
        print("Not a valid integer.Please try again")

#We ask the memebrs to input the number of cabohydrates grams they consumed in a day
#We use a while loop to create a loop that only breaks when the user inputs the right data type
#The if statement makes sure the input is a positive integer before the loop breaks.
#The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.

while True:
    try:
        carbs_gram = input("Input the number of carbohydrates grams: ")
        carbs_gram = int(carbs_gram)
        if carbs_gram < 0:
            print("Sorry, input must be a positive integer. Please try again")
            continue
        break
    except ValueError:
        print("Not a valid integer.Please try again")

#calculating the number of calories that result from the fat
calories_from_fat = fat_gram * 9

#calculating the number of calories that result from the carbohydrates
calories_from_carbs = carbs_gram * 4

#the quantitiy of the calories is measured in grams, so we input 'g' to ensure the quantity is read in grams
print('the number of calories in fats is:',calories_from_fat,'g')
print('the number of calories in carbohydrates is:',calories_from_carbs,'g')










