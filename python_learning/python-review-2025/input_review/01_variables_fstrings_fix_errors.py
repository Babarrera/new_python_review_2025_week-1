"""
Fix the Errors #1 — Variables & f-strings
Uncomment each block, fix it, and print a correct line to verify.
"""
# 1) Added quotes around pizza and fixed variable name inside f-string
food = "pizza"
print(f"You like {food}")

# 2) Added f before string so {age} is replaced with the variable value
age = 17
print(f"You are {age} years old")

# 3) This one was already correct — f-string and variable both good
price = 12.99
print(f"The total price is ${price}")

# 4) Fixed typo: changed 'dinstance' to 'distance'
distance = 5.5
print(f"You ran {distance} km")

# 5) Removed curly braces when using + to combine strings
name = "Bro"
print("Hello " + name)

# 6) Fixed mismatched quotes around the email string
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# 7) Changed variable name from 'class' to 'class_name' because 'class' is a reserved word in Python
class_name = "ECS"
print(f"You are in {class_name}")

# 8) Variable names can’t start with numbers, so changed '2cool' to 'cool2'
cool2 = "yes"
print(f"Am I cool? {cool2}")
