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

user_marks = int(input("Enter your Marks:"))
if user_marks >= 90:
    print("Grade A")
elif user_marks >= 75:
    print("Grade B")
elif user_marks >= 50:
    print("Grade C")
else:
    print("Grade F")