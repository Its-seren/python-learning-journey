# Lists 

- A list is a collection of multiple values in one variable
- Lists are ordered and changeable

Example:
numbers = [1, 2, 3, 4]

- Access elements using index (starts from 0)
Example:
numbers[0] -> 1

- Lists can store different data types
example:
data = [1, "hello", 3.5, True]
Here, 1 is an integer, hello is a string, 3.5 is a float, and True is a boolean

# Strings 

- Strings are sequences of characters
- Can yse single, double, or triple quotes
- Indexing works like lists (starts at 0)
- Common methods:
   - len(s) -> length
   - s.lower(), s.upper()
   - s.strip() -> removes space
   - s.replaced(old, new)
- Slicing: s[start:end] -> substring

# Dictionaries

- Dictionaries store data in key_value pairs
- Syntax: {key: value}

Example:
student = {"name": "Ali", "Age": 20}

- Access Vlues using keys:  student["name"] -> "Ali"

- Keys must be unique
- Values can be any data type

# File Handling
- used to read and write files
- open(filename, mode)

Modes:
- "r" -> read
- "w" -> write
- "a" -> append

Example:
file = open("data.txt", "w")
file.write("Hello")
file.close()

Better way:
with open("data.txt", "w") as file:
   file.write("Hello")