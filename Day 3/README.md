<h1>Door lock system Challenge – Task One (Day 3)<h1>
  <h2>Problem Statement</h2>

<p>Write a python program that simulates a door lock system such that:<br>
<ul>
<li>Password is set and stored in a variable</li>
<li>Commands to instruct the door are stored in variables.</li>
<li>When a user enters the wrong password an error message is displayed and prompted to enter the password again.</li>
<li>When a user enters “open” a “The door is now open” statement is displayed, when the “open” is entered more that once, a message is displayed saying, “the door is already open”</li>
<li>When a user enters “close” a “The door is now locked” statement is displayed, when the “open” is entered more that once, a message is displayed saying, “the door is already locked”</li>
<li>When a user enters “quit” the process is terminated and message is displayed.</li>
<li>When a wrong message is entered or invalid key pressed a “Invalid input” message is displayed.</li>
<li>When the door is locked or open, it prints out the last date/time the door was opened, eg “Door Last open  at 2022-07-05 08:46:20.535395”</li>
  </ul>
  </p>

<h2>Problem Definition</h2>
<h3>Steps taken to solve the poblem: Door lock system</h3>

<ul>
<li>We begin by importing the relevant module: the datetime module that we will use for our print outs
<ul><li>We need datetime library to print when the door was last opened or closed.</li></ul>
</li>
<li>We store our password in a variable named password 
<ul><li>Our password is set to admin</li></ul>
</li>
<li>We initialize some variables: open, close and quit</li>
<li>We ask the user to input the password</li>
<li>We use a while loop that only breaks when the user inputs the right password otherwise it runs an error message and reruns again</li>
<li>We then use an if elif statement to ask the user to enter a command then we determine the output</li>
</ul>

<h1>Calories from Fat and Carbohydrates: Challenge Task Two (Day 3)<h1>
<h2>Problem Statement</h2>
   
<p>A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula:<br>
  <ul>
<li>Calories from fats fat grams * 9</li>
    </ul>
Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
<ul>
    <li>Calories from carbs carb grams * 4</li>
</ul>
The nutritionist asks you to write a program that will make these calculation.

<h2>Problem Definition</h2>
<h3>Steps taken to solve the poblem: Calories from Fat and Carbohydrates</h3>
<ul>
<li>We ask the members to input the number of fat grams they consumed in a day
<ul>
<li>We use a while loop to create a loop that only breaks when the user inputs the right data type</li>
<li>The if statement makes sure the input is a positive integer before the loop breaks.</li>
<li>The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.</li>
</ul>
</li>
<li>
<ul>We ask the members to input the number of cabohydrates grams they consumed in a day
<li>We use a while loop to create a loop that only breaks when the user inputs the right data type</li>
<li>The if statement makes sure the input is a positive integer before the loop breaks.</li>
<li>The ValueError will prevent a stack trace from being displayed incase the user inputs data that is not of integer type.</li>
</ul>
</li>
<li>We calculate the number of calories that result from the fat by multiplying the fat gram by 9</li>
<li>We calculate the number of calories that result from the carbohydrates by multiplying the carb grams by 4</li>
<li>The quantitiy of the calories is measured in grams, so we input 'g' to ensure our output is printed with it appended at the end</li>
</ul>
