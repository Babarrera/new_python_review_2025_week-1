"""
Week 2 Day 1 — Working With Numbers and Strings in Python
--------------------------------------------------------
Concepts covered:
- Variables (strings + numbers)
- String concatenation and formatting (f-strings)
- String functions (len, upper, lower, replace, slice)
- Arithmetic (+ - * / % **, pow)
- Built-in math functions (max, min, round, abs)
- PEMDAS (order of operations)
- `math` module (floor, ceil, sqrt)
- Input from the user + basic calculator and Mad Libs challenge
"""

# --- STRING SECTION -------------------------------------------------------

print("Working with Strings:\n")

# String example 1
phrase = "python learning is ok"
print(phrase + " is cool")  # concatenation
print("Length of phrase:", len(phrase)) # length
print("Upper:", phrase.upper()) # upper case
print("Lower:", phrase.lower()) # lower case
# mini challenge: isupper and islower for students
#instructions are in comments below



new_first = "Isaac"
new_last = "Newton"
print("\nJoined name:", new_first + " " + new_last)

name = "your full name here"
print("\nOriginal name:", name) # replace with your full name \n for new line
print("Upper:", name.upper())
print("Lower:", name.lower())

# Checking upper/lower
print("\nIs name upper?", name.isupper())
print("Is phrase lower?", phrase.islower())

# Indexing and slicing
print("\nLast letter:", name[-1])
print("4th letter:", name[3])
print("8th letter:", name[7])

# Replacing words
print("\nReplacing last name:", name.replace("Evins", "Rodgers"))
print("Replacing first name:", name.replace("Marvin", "Steve"))

# Slicing range
print("Slice [2:6]:", name[2:6])

# Joining two variables
new_first = "Isaac"
new_last = "Newton"
print("\nJoined name:", new_first + " " + new_last)

# Challenge – Declaration of Independence snippet (UPPERCASE)
declaration = "when in the course of human events it becomes necessary..."
print("\nDeclaration UPPER:", declaration.upper())

# Variable naming rules review (comment discussion)
# 1. Cannot start with number
# 2. No spaces – use underscores
# 3. Avoid symbols like @, %, &
# 4. lowercase is best practice (PEP8)

# challenges: 
# create a new variable called name and set it to your full name
#print  your name in upper case and lower case
# print whether your name is in upper case and whether the phrase is in lower case
# print the last letter of your name, the 4th letter, and the 8th letter
# replace your last name with a different last name and print the result
# print the slice of your name from index 2 to index 6
# create two new variables called new_first and new_last and set them to a different first and last name
# print the joined version of new_first and new_last with a space in between    



# --- NUMBERS SECTION -----------------------------------------------------

# print("\nWorking with Numbers:\n")

# Basic arithmetic
# print("Addition:", 2 + 2)
# print("Multiplication:", 3 * 4)
# print("Division:", 12 / 6)
# print("Modulo (remainder):", 155 % 3)
# print("Powers:", 4 ** 3)
# print("Using pow():", pow(4, 3))

# Max/Min/Round/Abs
# print("Max:", max(4, 56, 67, 85, 93))
# print("Min:", min(4, 56, 67, 85, 93))
# print("Round:", round(95.2444))
# print("Absolute Value:", abs(-10))

# # Order of operations (PEMDAS)
# print("Order of Operations Result:", (4 + 5) / 9 - 8 + 8)

# # Math library
# from math import *


# # --- INPUT SECTION -------------------------------------------------------

# print("\nGetting Input From Users:\n")

# Example 1 – simple name input


# Example 2 – first + last name


# Example 3 – Basic Math Calculator

# Example 4 – Mad Libs Game


# --- STORY CHALLENGE ----------------------------------------------------

# print("\nStory Challenge — Variables Review\n")
# Create variables for age, name, song, food, and number
# Then create a short story using those variables and f-strings


