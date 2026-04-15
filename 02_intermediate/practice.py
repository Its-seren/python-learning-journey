# Problem 1 : create and Access List

# 1. Create a list of 5 numbers
# 2. Print: First element, last element

# Code:

# numbers = [8, 54, 89237, 11223, 23]
# print("First Element: ", numbers[0], "\nLast Element: ", numbers[4])

# -----------------------------------------------------------------------------------------------------

# Problem 2 : Modify List

# 1. Create a list of 5 numbers
# 2. Change the third element
# 3. Print the updated list

# Code:

# numbers = [8, 54, 89237, 11223, 23]

# print("Original List: ", numbers)

# numbers[2] = 2003

# print("Modified List:", numbers)

# -----------------------------------------------------------------------------------------------------

# Problem 3 : Add Elements to list

# 1. Create a list of 3 numbers
# 2. Add: One number using append(), one number using insert() (last element)
# 3. Print the list

# Code:

# myList = [23, 10, 2003]

# print("original List: ", myList)

# myList.append(2004) # append() adds at the end of the list
# myList.insert(2, 5) # insert() adds at the given index, here 2

# print("Updated List: ", myList)

# -----------------------------------------------------------------------------------------------------

# Problem 4 : Removes Elements from List

# 1. Create a list of 5 numbers
# 2. Remove: One number using remove(), one number using pop() (last element)
# 3. Print the list

# Code:

# myList = [23, 10, 2003]

# print("original List: ", myList)

# myList.remove(23) # remove() removes value 23
# myList.pop() # pop() removes last element

# print("Updated List: ", myList)

# -----------------------------------------------------------------------------------------------------

# Problem 5 : Loop through List 

# 1. Create a list of 5 numbers
# 2. Print each number squared using a for loop

# Code:

# anotherList = [1, 3, 76, 34, 23]

# for i in anotherList:
#     print(i, "squared is", i**2)


# -----------------------------------------------------------------------------------------------------

# Problem 1 : Basic String Access

# 1. Ask user for their name
# 2. Print First character, Lastt character, Total length

# Code:

# name = input("Enter your name: ")

# print("First Character of your name: ", name[0])
# print("Last Character of your name: ", name[-1])
# print("Length of your name: ", len(name))

# -----------------------------------------------------------------------------------------------------

# Problem 2 : String case conversion

# 1. Ask user for a sentence
# 2. Print all lowercase, All uppercase

# Code:

# sentence = input("Enter a sentence: ")
# print("All Lowercase: ", sentence.lower())
# print("All Uppercase: ", sentence.upper())

# -----------------------------------------------------------------------------------------------------

# Problem 3 : Remove Spaces

# 1. Ask user for a sentence with spaces at start/end
# 2. Remove extra spaces
# 3. Print cleaned text

# Code:

# sentence = input("Enter a sentence with spaces: ")

# cleaned = sentence.strip()

# print("Cleaned Sentence: ", cleaned)

# -----------------------------------------------------------------------------------------------------

# Problem 4 : Remove Spaces

# 1. Ask user for a sentence
# 2. Replace "bad" with "good"
# 3. Print updated sentence

# Code:

# text = input("Enter a sentence: ")

# updated = text.replace("bad", "good")

# print("Updated sentence: ", updated)

# -----------------------------------------------------------------------------------------------------

# Problem 5 : String Slicing

# 1. Ask user for a word
# 2. Print: First 3 characters and last 3 characters

# Code:

# word = input("Enter a word: ")

# print("First 3 Characters: ", word[:3])
# print("First 3 Characters: ", word[-3:])

# -----------------------------------------------------------------------------------------------------

# Problem 1 : Dictionary Basics

# 1. Create a Dictionary with: name, age, city
# 2. Print each value

# Code:

# student = {"name": "Seren", "age": 20, "city": "Doha"}

# print("Name:", student["name"])
# print("Age:", student["age"])
# print("City:", student["city"])

# -----------------------------------------------------------------------------------------------------

# Problem 2 : Modify Dictionary

# 1. Create a Dictionary with: name, age, city
# 2. Change the age
# 3. Print the updated dictionary

# Code:

# student = {"name": "Seren", "age": 20, "city": "Doha"}

# student["age"] = 25
# student["name"] = "Lily"

# print(student)

# -----------------------------------------------------------------------------------------------------

# Problem 3 : Add New Key

# 1. Create a Dictionary with name and age
# 2. Add a new key: "city"
# 3. Print the updated dictionary

# Code:

# student = {"name": "Seren", "age": 20}

# print(student)

# student["city"] = "Doha"

# print(student)

# -----------------------------------------------------------------------------------------------------

# Problem 4 : Loop Through Dictionary

# 1. Create a Dictionary with name, age and city
# 2. Use a loop to print: key and value

# Code:

# student = {"name": "Seren", "age": 20, "city": "Doha"}

# for key, value in student.items():
#     print(key, ":", value)

# -----------------------------------------------------------------------------------------------------

# Problem 5 : Check Key Exits

# 1. Create a Dictionary with name and age
# 2. Ask user for a key
# 3. Check if the key Exists
# 4. Print: "Key Exists", "Key not found"

# code:

# student = {"name": "Seren", "age": 20 }

# key = input("Enter a key to check: ")

# if key in student:
#     print("Key exists")
# else:
#     print("Key not found")

# -----------------------------------------------------------------------------------------------------

# Problem 1 : Write to File

# 1. Create a file data.txt
# 2. Write "Hello World" into it

# code:

# with open("data.txt", "w") as file:
#     file.write("Hello World!")

# -----------------------------------------------------------------------------------------------------

# Problem 2 : Read from file

# 1. Open data.txt
# 2. Read its content
# 3. Print it

# code:

# with open("data.txt", "r") as file:
#     dataInFile = file.read()

# print(dataInFile)

# -----------------------------------------------------------------------------------------------------

# Problem 3 : Append to file

# 1. Open data.txt in append mode
# 2. Add a new line: "Learning Python is fun"
# 3. Read and print full file content

# code:

# with open("data.txt", "a") as file:
#     file.write("\nLearning Pyhton is fun!!!!!")

# with open("data.txt", "r") as file:
#     dataInFile = file.read()

# print(dataInFile)

# -----------------------------------------------------------------------------------------------------

# Problem 4 : Count words in file

# 1. Open data.txt
# 2. Read the content
# 3. Count how many words are in the file
# 4. print the word count

# code:

# with open("data.txt", "r") as file:
#     content = file.read()

# words = content.split()

# print("Total words: ", len(words))

# -----------------------------------------------------------------------------------------------------

# Problem 5 : Copy file content

# 1. Read content from data.txt
# 2. Create a new file copy.txt
# 3. write the same content into copy.txt

# code:

with open("data.txt", "r") as file:
    content = file.read()


with open ("copy.txt", "w") as file:
    file.write(content)