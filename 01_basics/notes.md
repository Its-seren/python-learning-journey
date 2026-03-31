# Pyhton
Python is a programming language. It is used for web development, data analysis, automation, and more. Let's LEARN it!!!!!!!!!!!!

# Input & Output
- 'print()' is used to display output.
- 'input()' is used to get input from the user.

- NOTE!! Input is always a string by default.

# Converting Input 
- 'input()' always returns a string.
- Use 'int()' or 'float()' to convert input to numbers as age is taken in numbers.
- Convert input to numbers using 'int()' or 'float()' if or when needed.

# Variables and Data Types
- Variables store data. They act as containers for data.
- Common data types: int, float, str, bool
- Use 'type()' function to check a variable's data type.


# Operators
- Arithematic operators: + (Addition), - (Subtraction), * (Multiplication), / (Divison)
- % (Modulus gives the remainder)
- // (Floor Division give the integer result)

# User Input with Operations
- Convert input to int() or float() before calculations.
- We can perform arithematic operations on input numbers.

# Conditionals in Python
- conditionals allow our program to make decisions based on certain conditions.
## if Statement 
- Execute a block of code ** only if a condition is True **
## else Statement 
- Executes a block of code if the condition is False.
## elif (else if) statement 
- Check multiple conditions in order.
- use elif to check additional conditions if the previous if/elif was False.
- Helps aviod writing many nested if/else statements.
- example: Grading system using marks of students.

# Comparison Operators
- > : greater than
- < : less than
- >= : greater than or equal
- <= : less than or eqaul
- == : equal to
- != : not equal to

# Loops in Python
Loops are used to repeat a block of code multiple times.

## For Loop
- A for loop is used when we know how many times to repeat.
- Works with sequences like range(), lists, strings.    
- Example: range(1, 6) -> 1, 2, 3, 4, 
for i in range(1, 6):
    print(i)

## range() function
- range(start, end) ->  generates numbers from start to end-1
- range(start, end, step) -> step controls increment/decrement

Examples: 
range(1, 6) -> 1, 2, 3, 4, 5
range(0, 10, 2) -> 0, 2, 4, 6, 8
range(10, 0, -1) -> 10 down to 1

## Using Conditions in Loops
- We can use if statements inside loops.

Example:
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

## Accumulator Pattern
- Used to store results (like sum)

Example:
sum = 0
for i in range(1, 11):
    sum += i

## Loop Control
- break -> stops the loop completely
- continue -> skips current iteration

Example:
for i in range(5):
    if i == 3:
       break
    print(i)

# While Loop
A while loop is used to repeatedly execute a block of code as long as a condition remains True.

Example:
i = 1
while i <= 5:
    print(i)
    i += 1

Explanation:
- The loop starts with i = 1
- The condition (i <= 5) is checked beforee each iteration
- If the condition is True, the code inside the loop runs
- After each iteration, i is increased by 1
- The loop stops when the condition becomes False

Important Points:
- The condition must eventually become False, otherwise it creates an infinite loop
- Always update the loop variable inside the loop
- While loops are useful when the number of iterations is not fixed

# Difference B/W For Loop & While Loop
- In a for loop, the number of iterations is known beforehand.
- In a while loop, the loop runs based on a condition, not a fixed count.

# While Loop Practice (Guessing Game)
- While loops are useful for repeating until the correct condition is met.
- The loop continues until the user gives the correct answer.
- Common Use: games, input validation, etc

# Mini Project: Smart Calculator
- Combine loops, conditionals, and input/output.
- Uses while True for continues execution.
- Break is used to stop the loop.
- Useful for building real interactive programs.

# Functions
- Functions are reusable blocks of code
- Use 'def' to define a function
- Call the function to execute it
- Parameters let functions take input
- return lets functions send outputs back
- Local variables exist inside functions
- Global variables exit outside function
- Functions can have default values for optional inputs
- Functions make code organized and aviod repetition
- Functions are everywhere in Python: print(), input(), len(), etc.