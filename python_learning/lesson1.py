# This is a comment in python 
# variables are used to store data values
x = 5   #intger
y = 3.14  #float
name = "Benji" # string
# a letter is a list od characters in 
#qouatation makrks
is_student = True # boolean True or False
# Print the values of the varibles 
print(x) 
print(y)
print("Benji")
print(is_student)
#place in sentence without f-string
print("My name is " + name + ", I am " + str(x) + " years old.")
# the plus sign (+) is used to concatenate strings 
# str(x) coverts the integer x to a string
# type() function returns the type of a variable 
print(type((x))) #<class int>
print(type((y))) #<class 'float'>
print(type("Benji")) #<class 'str'>
print(type(is_student)) #<class 'bool'>
#lets make a new set of variables to practice 
a = 10
b = 2.5
c = "Benji"
d = False
#print the values of the new variables in a sentence
#using concation 
print(f"My name is {c}, I have {a} apples.")