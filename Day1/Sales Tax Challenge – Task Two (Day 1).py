
#We ask the user to input the square feet of wall to be painted.
#We use the while loop to build a loop that only breaks when a valid integer has been input.
#We use an if statement to check if the input is a positive integer before breaking the loop.
#The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.
#Stack trace is a valuable piece of information that we can use to debug our code.

while True:
       try:
              space_to_paint = input("Enter the square feet of wall space to be painted:")
              space_to_paint = int(space_to_paint)
              if space_to_paint < 0:  # if not a positive int print message and ask for input again
                     print("Sorry, input must be a positive integer, try again")
                     continue
              break
       except ValueError:
              print("Not a valid integer. Please try again") 

#We ask the user to enter the price of paint per gallon
#We use the while loop to build a loop that only breaks when a valid integer has been input.
#We use an if statement to check if the input is a positive integer before breaking the loop.
#The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.

while True:
       try:
              price_of_paint = input("Enter the price of paint per gallon:")
              price_of_paint = int(price_of_paint)
              if price_of_paint < 0:  # if not a positive int print message and ask for input again
                     print("Sorry, input must be a positive integer, try again")
                     continue
              break
       except ValueError:
              print("Not a valid integer. Please try again")

#• The number of gallons of paint required: is the space to paint divided by 115
paint_required = space_to_paint / 115
print("The number of gallons of paint required is:", paint_required)

#• The hours of labor required: is space to paint * 8 then ddivided by 115
hours__of_labor = (space_to_paint * 8)/115
print("The hours of labor required is:", hours__of_labor)

#• The cost of the paint: is the paint required * the price of paint
cost_of_paint = paint_required * price_of_paint
print("The cost of the paint is: $",cost_of_paint)

#• The labor charges: is the hours of labor *$20
labor_charges = hours__of_labor * 20.00
print("The labor charges are:$",labor_charges) 

#• The total cost of the paint job: is the sum of the cost of paint and the labor charges
total_cost = cost_of_paint + labor_charges
print("The total cost of the paint job is:$", total_cost)
