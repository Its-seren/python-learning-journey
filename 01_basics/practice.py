# print("Hello Worlds!")

# --------------------------------

# Problem 1 : Hello User

# 1. Ask the user for their name using input()
# 2. Print a greeting with their name.

# Code 1 : 

# name = input("Enter your name: ")
# print("Hello!", name, ".")

# --------------------------------

# Problem 2 : Age calculator

# 1. Ask the user for their Birth Year (as Input).
# 2. Calculate their age assuming the current Year is 2026.
# 3. print: "You are X years old."

# Code 2 : 
# birth_year = int(input("Enter your Birth Year: "))
# age = 2026 - birth_year
# print("You are", age, "years old.")

# --------------------------------------------------

# Problem 3 : Store and Print

# 1. Create 4 variables: my_name (name in string), my_age (age in int), height (height in foots and inches), is_student (true or false in Boolean).
# 2. Print each variable and its type.

# Code 3 :

# my_name = "Seren"
# my_age = 20
# height = 5.3
# is_student = True

# print(my_name, type(my_name))
# print(my_age, type(my_age))
# print(height, type(height))
# print(is_student, type(is_student))

# --------------------------------------------------

# Problem 4 : Simple Operations

# 1. Create two variables (a and b)
# 2. Print the result of: addition, subraction, multiplication, division, modulus, floor division.

# Code 4 :

# a = 2
# b = 12

# print("Addition:", a+b)
# print("Subtraction:", a-b)
# print("Multiplication:", a*b)
# print("Divison:", a/b)
# print("Modulus:", a%b)
# print("Floor Division:", a//b)

# ---------------------------------------------------------------------

# Problem 5 : user Input with Operations

# 1. Ask the user to input two numbers.
# 2. Calculate and print: Sum, Difference, Product, Divison.

# Code 5 :

# num1 = float(input("Enter the First number: "))
# num2 = float(input("Enter the Second number: "))

# print("Sum: ", num1 + num2)
# print("Difference: ", num1 - num2)
# print("Product: ", num1 * num2)
# print("Division: ", num1 / num2)

# -----------------------------------------------------------

# Problem 6 : Age Check

# 1. Ask the user for their age.
# 2. If age >= 18 (print "You are an adult.").
# 3. Else (print "You are a minor.")

# Code 6 :

# user_age = int(input("Enter Your Age: "))

# if user_age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")

# ----------------------------------------------------------------------

# Problem 7 : Grading System

# 1. Ask the user for their marks.
# 2. Print grade based on: 90+ (Grade A), 75-89 (Grade B), 50-74 (Grade C), Below 50 (Grade F).

# Code 7 :

# user_marks = int(input("Enter your Marks:"))
# if user_marks >= 90:
#     print("Grade A")
# elif user_marks >= 75:
#     print("Grade B")
# elif user_marks >= 50:
#     print("Grade C")
# else:
#     print("Grade F")

# ------------------------------------------------------------------------

# Problem 8 : For Loop Basics

# 1. Use a for loop
# 2. Print numbers from 1 to 5

# Code 8 :

# for i in range(1, 6):
#     print(i)

# ------------------------------------------------------------------------

# Problem 9 : For Loop Calculations

# 1. Use a for loop
# 2. Print numbers from 1 to 10
# 3. Also print their square

# Code 9 :

# for i in range(1, 11):
#     print(i)
#     print("Square is", i**2)
#     print(i, ", The Square of ", i , "is", i*i ,"." )

# ------------------------------------------------------------------------------------

# Problem 10 : For Loop Calculations

# 1. Use a for loop
# 2. Print even numbers from 1 to 20

# Code 10 :

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

#------------------------------------------------------------------------

# Problem 11 : For Loop Calculations

# 1. Use a for loop
# 2. Find the sum of numbers from 1 to 10
# 3. Print the final sum

# Code 11 :

# sum = 0
# for i in range(1,11):
#     sum += i
#     print("Sum:", sum)

# -------------------------------------------------------

# Problem 12 : Countdown

# 1. Print numbers from 10 to 1 using a loop

# Code 12 :

# for i in range(10, 0, -1):
#     print(i)

# -----------------------------------------------------------------

# Problem 13 : While Loop

# 1. Use a while loop
# 2. Print numbers from 1 to 5

# Code 13 :

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# -----------------------------------------------------------

# Problem 14 : Loop until Exit

# 1. Keep asking the user to enter something
# 2. Stop only when the user types "exit"
# 3. Print whatever the user enters (except "exit")

# Code 14 :

# user_input = ""

# while user_input != "exit":
#     user_input = input("Type something (or 'exit' to stop): ")
#     if user_input != "exit":
#         print("You entered :", user_input)

# -------------------------------------------------------------

# Problem 15 : Number Guessing

# 1. Set a secret number: 7
# 2. Ask the user to guess the secret number
# 3. Keep asking until they guess correctly
# 4. If wrong -> Print "Try Again"
# 5. If correct -> Print "Correct!" and stop.

# Code 15 :

# secret_number = 7
# guess = 0

# while guess != secret_number:
#     guess = int(input("Guess the number: "))
#     if guess != secret_number:
#         print("try Agian!")

# print("Correct!")

# -------------------------------------------------------------

# Problem 16 : Smart Calculator

# 1. Show options to the user: add, subtract, multiply, divide, exit.
# 2. Ask the user to choose an operation
# 3. Ask for two numbers
# 4. Perform the operation
# 5. Show result
# 6. Repeat until user types "Exit"

# Code 16 :

# while True:
#     opr = input("Select an operation (+, -, *, /, and Exit): ")

#     if opr == "Exit":
#         print("Calculation Stopped.")
#         break

#     num1 = float(input("Enter the First number: "))
#     num2 = float(input("Enter the Second number: "))

#     if opr == "+":
#         print("Sum: ", num1 + num2)
#     elif opr == "-":
#         print("Sum: ", num1 - num2)
#     elif opr == "*":
#         print("Sum: ", num1 * num2)
#     elif opr == "/":
#         print("Divison: ", num1 / num2)
#     else:
#         print("Invalid Input!!")

# -------------------------------------------------------------

# Problem 17 : First function

# 1. Create a function
# 2. Inside it, print "Hello, welcome!"
# 3. Call the function to see the output

# Code 17 :

# def hello():
#     print("Hello, welcome!")

# hello()

# -------------------------------------------------------------

# Problem 18 : Function with Parameter

# 1. Create a function called greet_user that takes one parameter name
# 2. Print "Hello, <name!>" inside the function
# 3. Call the function with at least 2 different names

# Code 18 :

# def greet_user(name):
#     print("Hello,", name,"!") # I can also print("Hello,", name + "!"), the plus'+' removes the blank space b/w the name and !.

# greet_user("Seren")
# greet_user("Lily")

# -------------------------------------------------------------

# Problem 19 : Add two numbers with a Function

# 1. Create a function called add that takes two parameters a and b
# 2. The function should return the sum of a and b
# 3. Call the function with different numbers and print the result

# Code 19 :

# def add(a, b):
#     return a+b

# print("The sum of 3 and 4 is ", add(3, 4))
# print("The sum of 5 and 7 is ", add(5, 7))

# -------------------------------------------------------------

# Problem 20 : Even and Odd checker with a Function

# 1. Create a function called is_even that takes one number as a parameter
# 2. The function should return True if the number is even, else False
# 3. Call the function with different numbers and print the result

# Code 20 :

# def is_even(n):
#     if n % 2 == 0:
#         return "True"
#     else:
#         return "False"
    
# print("Is the number 12 even?", is_even(12))
# print("Is the number 3 even?", is_even(3))
# print("Is the number 823213 even?", is_even(823213))

# -------------------------------------------------------------

# Problem 21 : Square of a Number with a function

# 1. Create a function called square that takes one number n as a parameter
# 2. The function should return the square of the number
# 3. Call the function with different values and print results

# Code 21 :

# def square(n):
#     return n**2

# print("The square of 2 is", square(2))
# print("The square of 45 is", square(45)) # woww!! I got 2025 as an answer ;)>
# print("The square of 3 is", square(3))

# -------------------------------------------------------------

# Problem 22 : Largest of Three Numbers with a Function (ya, agian with a function)

# 1. Create a function called largest that takes three number: a, b, c as a parameter
# 2. The function should return the largest number
# 3. Call the function with different values and print results

# Code 22 :

# def largest(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print("The largest is ", largest(1, 4, 2))
# print("The largest is ", largest(5, 6, 21))
# print("The largest is ", largest(3, 44, 22))

# -------------------------------------------------------------

# Problem 23 : Smart Calculator with functions
# 1. Create separate Functions: add() for addition, sub() for subtraction, mul() for multiplication, and div() for division.
# 2. Show options to the user: add, subtract, multiply, divide, exit.
# 3. Ask the user to choose an operation
# 4. Ask for two numbers (num1, num2)
# 5. Perform the operation
# 6. Show result
# 7. Repeat until user types "Exit" (While Loop)

# Code 23 :

# def add(num1, num2):
#     return num1 + num2

# def sub(num1, num2):
#     return num1 - num2

# def mul(num1, num2):
#     return num1 * num2

# def div(num1, num2):
#     return num1 / num2

# while True:
#     opr = input("Select an operation (+, -, *, /, and Exit): ")

#     if opr == "Exit":
#         print("Calculation Stopped.")
#         break

#     num1 = float(input("Enter the First number: "))
#     num2 = float(input("Enter the Second number: "))

#     if opr == "+":
#         print("Sum: ", add(num1, num2)) # small change here
#     elif opr == "-":
#         print("Sum: ", sub(num1, num2)) # small change
#     elif opr == "*":
#         print("Sum: ", mul(num1, num2)) # small change
#     elif opr == "/":
#         print("Divison: ", div(num1, num2)) # small change
#     else:
#         print("Invalid Input!!")