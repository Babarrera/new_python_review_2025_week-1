# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")

# Get two numbers from the user and ask for their name to personalize the experience

print("Welcome! We'll do some math.\n")

# Ask for the user's name
name = input("What's your name? ")

# Ask for two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the inputs to floats so we can do math
num1 = float(num1)
num2 = float(num2)

# Show the student notes in action:
print(f"\nThanks, {name}! Let's do some calculations with {num1} and {num2}.\n")

# Addition
sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result:.2f}")

# Subtraction
sub_result = num1 - num2
print(f"{num1} - {num2} = {sub_result:.2f}")

# MultiplicationBig 
mul_result = num1 * num2
print(f"{num1} * {num2} = {mul_result:.2f}")

# Division (check for division by zero)
if num2 != 0:
    div_result = num1 / num2
    print(f"{num1} / {num2} = {div_result:.2f}")
else:
    print("Cannot divide by zero!")

# Exponent
exp_result = num1 ** num2
print(f"{num1} raised to the power of {num2} = {exp_result:.2f}")

# Ask for user's birthday
birthday = input("What is your birthday? ")

# Ask for user's favorite food
favorite_food = input("What is your favorite food? ")

# Print a response using the inputs
print("Cool! Your birthday is on", birthday, "and you love", favorite_food + "!")











# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings