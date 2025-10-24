first_name = "Bro"      # string
food = "pizza"          # string
email = "Bro123@fake.com"  # string
age = 25                # integer
quantity = 3            # integer
price = 10.99           # float
gpa = 3.2               # float
distance = 5.5          # float

print(f"Hello {first_name}")        # Hello Bro
print(f"You like {food}")           # You like pizza
print(f"Your email is: {email}")    # Your email is: Bro123@fake.com
print(f"You are {age} years old")  # You are 25 years old
print(f"You are buying {quantity} items")  # You are buying 3 items
print(f"The price is ${price}")     # The price is $10.99
print(f"Your GPA is {gpa}")        # Your GPA is 3.2
print(f"You ran {distance} km")    # You ran 5.5 km

# Original: name = Bro
# Original: food = pizza
# Issue: Missing quotes around strings
name = "Bro"          # string
food = "pizza"        # string
print(f"Hello {name}")
print(f"You like {food}")

# Original: food = pizza; print(f"You like {favorite_food}")
# Issue: variable name mismatch and missing quotes
favorite_food = "pizza"
print(f"You like {favorite_food}")

# Original: age = 17; print("You are {age} years old")
# Issue: forgot f-string
age = 17
print(f"You are {age} years old")

# Original: price = 12.99; print(f"The total price is ${price}"
# Issue: missing closing parenthesis
price = 12.99
print(f"The total price is ${price}")

# Original: name = "Bro"; print("Hello " + {name})
# Issue: {} not needed when using +; use variable directly
name = "Bro"
print("Hello " + name)

# Original: email = "Bro123@fake.com'
# Issue: mismatched quotes
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# Original: age = 21; print("You are {age} years old")
# Issue: forgot f-string
age = 21
print(f"You are {age} years old")

# Original: 2cool = "yes"; print(f"Am I cool? {2cool}")
# Issue: variable cannot start with a number
cool2 = "yes"
print(f"Am I cool? {cool2}")

# Original: quantity = 3; print(f"You are buying quantity items")
# Issue: missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Original: class = "ECS"; print(f"You are in {class}")
# Issue: 'class' is a reserved keyword
class_name = "ECS"
print(f"You are in {class_name}")





# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")

# Part 4 – Create Your Own

# Step 1: Create a string variable
# This variable will store the name of a favorite book
book = "Harry Potter"

# Step 2: Create an integer variable
# This variable will store the year the book was published
year_published = 1997

# Step 3: Create a float variable
# This variable will store the average rating of the book
rating = 4.8

# Step 4: Print a formatted message combining all three variables
# We use an f-string (f"") which allows us to embed variables directly inside the string
# Curly braces {} are used to insert the values of variables into the text
print(f"My favorite book is '{book}', published in {year_published}, with a rating of {rating}/5!")

# Explanation:
# - 'book' is a string variable holding text
# - 'year_published' is an integer variable holding a whole number
# - 'rating' is a float variable holding a decimal number
# - f-strings make it easy to create readable messages that include multiple types of data
