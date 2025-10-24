# """
# Fix the Errors #2 — Input & Math
# """

# # A) Original problem:
# #    - input() gives text, so x + y would join strings instead of adding numbers.
# #    - Need to convert to int or float for math.
# x = float(input("Enter a number: "))   #  Changed: added float() to convert input to number
# y = float(input("Enter another number: "))  #  Same reason here
# print(f"Sum: {x + y}")   #  Now adds correctly as numbers, not text

# # B) Original problem:
# #    - Missing a closing quote in the input prompt.
# #    - f-string was missing, so {int(age) + 10} didn’t evaluate.
# #    - Better to convert age to int immediately after input.
# age = int(input("How old are you? "))  #  Fixed missing quote and converted to int
# print(f"In 10 years you will be {age + 10}")  #  Added f before string to evaluate expression

# # C) Original problem:
# #    - This one was already correct!
# #    - Both inputs converted to float so math works fine.
# n = float(input("Enter a numerator: "))
# d = float(input("Enter a denominator: "))
# result = n / d
# print(f"Result: {result}")  #  No change needed

# # D) Original problem:
# #    - ^ does NOT mean power in Python (it means bitwise XOR).
# #    - // does integer division, not remainder. Should use % for remainder.
# a = 5
# b = 2
# print(f"Power: {a ** 2}")    #  Changed ^ to ** for exponent
# print(f"Remainder: {a % b}") #  Changed // to % for remainder

# # E) Original problem:
# #    - No errors here, already works fine.
# pi = 3.1415926535
# print(f"Pi is approximately {pi}")  #  No changes made

x = 1
Y = 2
Z = 3
result = (x + Y) * Z - (Y/x)
print(f"Result: {result}")

#pemdas order of operations

# Basic Math in Python

# Ask the user for two numbers
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

# Perform math operations
# print("\n--- Basic Math ---")
# print(f"Addition: {x} + {y} = {x + y}")
# print(f"Subtraction: {x} - {y} = {x - y}")
# print(f"Multiplication: {x} * {y} = {x * y}")
# print(f"Division: {x} / {y} = {x / y}")
# print(f"Exponent (x^y): {x} ** {y} = {x ** y}")
# print(f"Remainder (x % y): {x} % {y} = {x % y}")

# #  Basic Arithmetic
# x, y = 10, 3
# print("Addition:", x + y)
# print("Subtraction:", x - y)
# print("Multiplication:", x * y)
# print("Division:", x / y)
# print("Floor Division:", x // y)
# print("Modulus:", x % y)
# print("Exponentiation:", x ** y)

# #  Math Module
# import math
# print("\nMath Constants:", math.pi, math.e)
# print("Square Root:", math.sqrt(16))
# print("Factorial:", math.factorial(5))
# print("Trigonometry (sin 90°):", math.sin(math.radians(90)))
# print("Logarithm base e:", math.log(10))
# print("Ceil and Floor:", math.ceil(4.2), math.floor(4.2))

# #  Statistics Module
# import statistics
# data = [1, 2, 3, 4, 5, 5]
# print("\nMean:", statistics.mean(data))
# print("Median:", statistics.median(data))
# print("Mode:", statistics.mode(data))
# print("Standard Deviation:", statistics.stdev(data))

# #  NumPy
# import numpy as np
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])
# print("\nDot Product:", np.dot(a, b))
# print("Element-wise Sum:", a + b)
# print("Matrix Multiplication:", np.matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

# #  SymPy
# import sympy as sp
# x = sp.symbols('x')
# expr = x**2 - 4
# solutions = sp.solve(expr, x)
# print("\nSolving Equation x² - 4 = 0:", solutions)
# print("Derivative of x²:", sp.diff(x**2, x))
# print("Integral of x:", sp.integrate(x, x))

# #  SciPy
# from scipy import integrate, optimize
# result = integrate.quad(lambda x: x**2, 0, 1)
# print("\nIntegral of x² from 0 to 1:", result[0])
# root = optimize.root(lambda x: x**2 - 4, x0=1)
# print("Root of x² - 4:", root.x)

# #  Random Module
# import random
# print("\nRandom Float:", random.random())
# print("Random Integer (1-10):", random.randint(1, 10))
# print("Random Choice:", random.choice(['apple', 'banana', 'cherry']))
# items = [1, 2, 3, 4]
# random.shuffle(items)
# print("Shuffled List:", items)

# #  Decimal and Fractions
# from decimal import Decimal
# from fractions import Fraction
# print("\nDecimal Precision:", Decimal('0.1') + Decimal('0.2'))
# print("Fraction Addition:", Fraction(1, 3) + Fraction(1, 6))

x = 1
y = 2
z = 3
result= (x+y)* z -(y/x)
print(f"result:{result}")
print(f"division:{y/x}")
print(f"addition:{x+y}")
print(f"multiplication:{(x+y)*z}")
print(f"subtraction: {(x+y)*z-(y/x)}")
print(f"modulo:{y%x}")
print(f"power:{x**y}")
print(f"absolute value:{abs(x-y)}")
print(f"max{max(x,y,z)}")
print(f"min:{min(x,y,z)}")
pi=3.1415926535
print(f"round:{round(pi)}")
from math import*
print(f"square root of 16:{round(16)}")
print(f"ceiling of pi:{ceil(pi)}")
print(f"floor of pi:{floor(pi)}")