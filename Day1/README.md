<h1>Bus Fare Challenge – Task One (Day 1)</h1>
<h2>Problem Statement.</h2>
<p>Write a program that does the following:<br>
  <ol>
<li>Gets today's date and stores it in a variable 'date'</li>
<li>Uses today's date to get the name on the day of the week written in short form with the first letter capitalized eg. 
  'Fri' if today were Friday and assigns it a variable 'day'</li>
<li>Uses if statements to determine the today's fare following these bus fare schedule:
  <ul>
    <li>Monday - Friday --> 100</li>
    <li>Saturday --> 60</li>
    <li>Sunday --> 80</li>
   </ul>
</li>
<li>Prints the results in this format 
Date: 2022-07-05
Day: Tue
Fare: 100
</li>
   </ol>
</p>
<h2>Problem Definition</h2>
<h3>Steps Taken to solve the problem: Bus Fare Challenge</h3>
<ul>
<li>We began by importing the relevant module: Datetime </li>
<li>We used the datetime module to get todays date and store it in a variable date then printed it out</li>
<li>Using todays date that we had generated, we get the name on the day of the week written in short form with the first letter capitalized,
we achaived this by using the right date to string format and then printed it out</li>
<li>Using the weekday() method, we used an if statements to determine the today's fare based on weather it was a weekday, Saturday or Sunday then 
printed it out</li>
</ul>



<h1>Sales Tax Challenge – Task Two (Day 1)</h1>
<h2>Problem Statement.</h2>
 <p>A painting company has determined that for every 115 square feet of wall space, one gallon of paint and eight hours of labor will be required.
 The company charges $20.00 per hour for labor.
 Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon.<br>
 The program should display the following data:<br>
  <ul>
<li>The number of gallons of paint required</li>
<li>The hours of labor required</li>
<li>The cost of the paint</li>
<li>The labor charges</li>
<li>The total cost of the paint job</li>
    </ul>
</p>

<h2>Problem Definition</h2>
<h3>Steps Taken to solve the problem: Sales Tax Challenge</h3>
<ul>
<li>We ask the user to input the square feet of wall to be painted.
  <ul>
    <li>We use the while loop to build a loop that only breaks when the user inputs a valid integer.</li>
    <li>We use an if statement to check if the input is a positive integer before breaking the loop.</li>
    <li>We use the ValueError to prevent a stack trace from being displayed incase the user inputs data that is not of integer type.</li>
    <li>Stack trace is a valuable piece of information that we can use to debug our code.This is not very understandable to a non-programmer.</li>
    </ul>
</li>

<li>We ask the user to enter the price of paint per gallon.
  <ul>
    <li>We use the while loop to build a loop that only breaks when the user inputs a valid integer.</li>
    <li>We use an if statement to check if the input is a positive integer before breaking the loop.</li>
    <li>We use the ValueError to prevent a stack trace from being displayed incase the user inputs data that is not of integer type.</li>
    <li>Stack trace is a valuable piece of information that we can use to debug our code.This is not very understandable to a non-programmer.</li>
    </ul>
</li>

<li> The number of gallons of paint required is the space to paint divided by 115</li>
<li>The hours of labor required is space to paint * 8 then divided by 115</li>
<li>The cost of the paint is the paint required * the price of paint</li>
<li>The labor charges is the hours of labor *$20</li>
<li>The total cost of the paint job is the sum of the cost of paint and the labor charges</li>
</ul>


