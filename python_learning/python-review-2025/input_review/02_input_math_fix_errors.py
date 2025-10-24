"""
Fix the Errors #2 — Input & Math
"""

# A) Original problem:
#    - input() gives text, so x + y would join strings instead of adding numbers.
#    - Need to convert to int or float for math.
x = float(input("Enter a number: "))   #  Changed: added float() to convert input to number
y = float(input("Enter another number: "))  #  Same reason here
print(f"Sum: {x + y}")   #  Now adds correctly as numbers, not text

# B) Original problem:
#    - Missing a closing quote in the input prompt.
#    - f-string was missing, so {int(age) + 10} didn’t evaluate.
#    - Better to convert age to int immediately after input.
age = int(input("How old are you? "))  #  Fixed missing quote and converted to int
print(f"In 10 years you will be {age + 10}")  #  Added f before string to evaluate expression

# C) Original problem:
#    - This one was already correct!
#    - Both inputs converted to float so math works fine.
n = float(input("Enter a numerator: "))
d = float(input("Enter a denominator: "))
result = n / d
print(f"Result: {result}")  #  No change needed

# D) Original problem:
#    - ^ does NOT mean power in Python (it means bitwise XOR).
#    - // does integer division, not remainder. Should use % for remainder.
a = 5
b = 2
print(f"Power: {a ** 2}")    #  Changed ^ to ** for exponent
print(f"Remainder: {a % b}") #  Changed // to % for remainder

# E) Original problem:
#    - No errors here, already works fine.
pi = 3.1415926535
print(f"Pi is approximately {pi}")  #  No changes made
