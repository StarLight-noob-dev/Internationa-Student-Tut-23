__author__ = "<student number>, <name>"

import turtle
import random

# Type hinting is a good way to understand what is being taken and returned at all point
# but is not neccesary and do almost nothing till Python3.12 or so.

def decimal_to_basis(number:int, base:int=2)->str:
    """
    Takes a decimal number and convert it into its representation in the given basis
    if no basis was given it will turn the number in its binary version
    @param: number, has to be decimal.
    @param: base, any number bigger 2, default is 2
    """
    
    decimal_number = int(number)  # In order to ensure integer.
    
    if decimal_number == 0:
        print("The decimal number 0 is 0 in base: {base}")
        return "0"
    elif decimal_number < 0 or base < 2:
        print("Number is negative, impossible to tranform into the base")
        return "wrong entry"  # throw exception not yet introduced

    # store the initial value of the decimal number
    dez = decimal_number

    # variable to store the binary representation
    changed_number = ""

    while decimal_number > 0:
        # get remainder when dividing by basis
        remainder = decimal_number % base

        # place remainder in front of the binary representation
        changed_number = str(remainder) + changed_number

        # print this steps calculation
        # with format string.
        print(f"{decimal_number} / {base} = {decimal_number} // {base},  Rest {remainder}")
        
        # with String.format()
        #print("{} / {} = {} // {}, Rest {}".format(decimal_number, base, decimal_number, base, remainder))
        
        # divide decimal number  '//' is Floor Division
        decimal_number //= base
    print(f"The decimal number {dez} is {changed_number} in base {base}")
    return changed_number


def decimal_to_octal(n:int)->str:
    """
    Return the given number into basis 8
    @param: n, number to be transformed
    """
    return decimal_to_basis(n, 8)


def chaos_turtle(x=100, y=100, iterations=1000):
    """ This function generates a turtle drawing panel and draws points \
        based on a rectangle and random movements.
    """

    # three points of a rectangle
    a = (-200, -200)  # bottom left
    b = (400, -200)  # bottom right
    c = (100, 400)  # upper

    turtle.speed(0)
    turtle.up()
    turtle.goto(x, y)

    while iterations > 0:
        i = random.randint(1, 3)
        position = turtle.pos()
        x = position[0]
        y = position[1]
        if i == 1:  # to a
            x = (x + a[0]) / 2
            y = (y + a[1]) / 2
        if i == 2:  # to b
            x = (x + b[0]) / 2
            y = (y + b[1]) / 2
        if i == 3:  # to c
            x = (x + c[0]) / 2
            y = (y + c[1]) / 2

        turtle.goto(x, y)
        turtle.dot(3, 'green')
        iterations -= 1
if __name__ == '__main__':
    # Testcases:
    # decimal_to_octal
    if decimal_to_octal(-4) == "wrong entry":
        print("decimal_to_octal for -4: OK")
    else:
        print("decimal_to_octal for -4: FAILED")
    if decimal_to_octal(0) == "0":
        print("decimal_to_octal for 0: OK")
    else:
        print("decimal_to_octal for 0: FAILED")
    if decimal_to_octal(44) == "54":
        print("decimal_to_octal for 54: OK")
    else:
        print("decimal_to_octal for 54: FAILED")

        # decimal_to_basis
    if decimal_to_basis(-4, 5) == "wrong entry":
        print("decimal_to_basis for -4 (basis: 5): OK")
    else:
        print("decimal_to_basis for -4 (basis: 5): FAILED")
    if decimal_to_basis(8, -5) == "wrong entry":
        print("decimal_to_basis for 8  (basis: -5): OK")
    else:
        print("decimal_to_basis for 8  (basis: -5): FAILED")
    if decimal_to_basis(54, 5) == "204":
        print("decimal_to_basis for 54 (basis: 5): OK")
    else:
        print("decimal_to_basis for 54 (basis: 5): FAILED")

    # To test this just call once to see if it works.
    chaos_turtle(iterations=10)