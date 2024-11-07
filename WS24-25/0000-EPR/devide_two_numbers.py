__author__ = "Calderon, 7727995"

# Takes the inputs
a = int(input("Please give the dividend: ")) # Explicit type casting is safer
b = eval(input("Please give the divisor: "))

quotient = a // b # / vs // the second one is a floor division

remainder = a % b # % is the Modulo operator 3%2=1

# Output
#print("The integer quotient of the division of ", a, " and ", b, " is: ", quotient)
#print("The remainder of the division of ", a, " and ", b, " is: ", remainder)

# Please learn F-String it can simplify your work
print(f"The integer quotient of the division of {a} and {b} is: {quotient}")
print(f"The remainder of the division of {a} and {b} is: {remainder}")

# Example taken from professor
# a: 32 b: 3 --> quotient 10 und remainder 2
# a: 0 b: 5 --> harm 0 und arithm 0
# a: 5 b: 8 --> harm 0 und arithm 5
# a: 15 b: 0 --> ZeroDivisionError: integer division or modulo by zero

# Upload the doku example
# Sources : https://docs.python.org/3/