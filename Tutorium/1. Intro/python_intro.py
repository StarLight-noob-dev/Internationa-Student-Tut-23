__author__ = "7727995, Calderon"

###########################################################################
#
#   Python is a high level language
#   Dynamically typed: Type checking occurs as code runs (types can change)
#
###########################################################################

# Download VS Code:     https://code.visualstudio.com/
# Download Python:      https://www.python.org/downloads/
# Settings -> Rulers <"editor.rulers": [100]>

# Stop 65, 80, 100

# What Are Variables In Python?

# A variable is a memory location where you store a value.
# The value that you have stored may change in the future according
# to the specifications

# A Variable in python is created as soon as a value is assigned to it.
# It does not need any additional commands to declare a variable in python.


# Variable Definition & Declaration
x = 16
# Variable is declared as the value 16 is assigned to it.

# Rules when declaring variable
# 1. The variable name cannot start with a number.
# 2. It can only start with a character or an underscore.
# 3. Variables in python are case sensitive.
# 4. They can only contain alpha-numeric characters and underscores.
# 5. No special characters are allowed.



# Data Types In Python

# INTEGERS (int): are used to represent whole number values.
x = 100
y = 124
# it will be the integer as long as the value is a whole number.

# To check the type of any variable data type, we can use the type() function.
# It will return the type of the mentioned variable data type.


# FLOAT (float): is used to represent decimal point values.
x  = 10.25
y = 12.30


# COMPLEX NUMBERS (complex): are used to represent imaginary values.
# Imaginary values are denoted with ‘j’ at the end of the number.
x = 10 + 5j


# BOOLEAN (bool): is used for categorical output, since the output of
# boolean is either true or false.
num = 23 < 13
#num is the boolean variable
type(num)
#the output will be bool
print(num)
#this will print False.
True == 1 
False == 0



# Strings (str): in python are used to represent unicode character values.
# Python does not have a character data type,
# a single character is also considered as a string.

# We denote or declare the string values inside single quotes or double
# quotes. To access the values in a string,
# we use the indexes and square brackets.

#str = ""
#char = ''


name = 'eureka'
print(name[2])
#this will give you the output as 'r'
# Strings are immutable in nature, which means you cannot change a string
# once replaced. 



# LIST: is ordered and changeable, unlike strings.
# We can add duplicate values as well. To declare a list we use the
# square brackets.

mylist = [10,20,30,40,20,30, 'edureka']



# SETS: set is a collection which is unordered, 
# it does not have any indexes as well.
# To declare a set in python we use the curly brackets.

myset = {10, 20 , 30 ,40, 50, 50}
print(myset)


# TUPLES: is a collection which is unchangeable or immutable

mytuple = (10,10,20,30,40,50)


# DICTIONARY: is just like any other collection array in python.
# But they have key value pairs

mydictionary = { 'python': 'data science', 'machine learning' : 'tensorflow' , 'artificial intelligence': 'keras'}
 
print(mydictionary['machine learning'])
 
#this will give the output as 'tensorflow'
 
mydictionary.get('python')
 
#this serves the same purpose to access the value.



# Get user input

user_answer = input("What is your name?")    # input always return a str. How can we change it?
user_answer[2:4]

print(f"Hello {user_answer}")