# Pyhton
Python is a programming language. It is used for web development, data analysis, automation, and more. Let's LEARN it!!!!!!!!!!!!

# Basic Topics 
1. Input / Output
- Taking input - input()
- Formatting output - print()
- type conversion (int(), float())

2. Variables and Data Types
- int, float, string, boolean
- type()

3. Operatores
- arithmetic operators (+, -, *, /, %(modulus), **(exponent), //(floor division))
- comparison operators (==(equal to), !=(Not equal to), >(greater than), <(less than), >=(Greater than or equal to), <=(less than or equal to))
- Assignment Operators (=(assign value), +=(add and assign), -=(subtract and assign), *=(multiply and assign), /=(divide and assign), %=(modulus and assign), **=(exponnet and assign), //=(flooar division and assign))
- Logical Operators (and (returns True if both conditions are true), or (returns True if at least one condition is true), not (reverses the result(True becomes False, and vice versa)))
- Bitwise Operators
- Membership operators
- Identity operators

4. Conditional Statements
- if, else, elif
- Nested Conditons

6. Loops
- for loop
- while loop
- break, continue, pass
- range()
- loop + condition
- loop + counter

7. Functions
- defining functions def()
- basic function
- parameters and return values
- multiple arguments

------------------------------------------------------------------------

# comments 
- Comments are used to explain code 
- They are ignored by Python
- Single-line comment starts with #
- example: # This is a comment

# Input & Output
- 'print()' is used to display output.
- 'input()' is used to get input from the user.

- NOTE!! Input is always a string by default.

# Converting Input 
- 'input()' always returns a string.
- Use 'int()' or 'float()' to convert input to numbers as age is taken in numbers.
- Convert input to numbers using 'int()' or 'float()' if or when needed.

# Type casting
- converting one data type to another
- int(), float(), str()
-Example: num = int("5") # Here 5 is treated as a string

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

# Basic Error Handling
- Division by zero causes error
- Invalid input (like letters in int) causes error
- Programs can crash if not handled

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