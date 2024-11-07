import epr_functions_tutorium as tut

def menu():
    """
    Menu to choose what functions to call
    """

    while True:
        choice = input("What would you like to do?\n 1: Calculate the octagonal basis of a number\n 2: Change a number into base n\n 3: Draw some chaos? ;)\n q: Close the application\n -> ")

        match choice:
            case "1":
                call_octal()
            case "2":
                call_base()
            case "3":
                call_chaos()
            case "q":
                break
            case _:
                print("Looks like there has been a miss-input, please try again. The options are " +
                      "the characters before ':'")

def call_octal():
    """
    Call the decimal_to_octal function from import
    """
    n = int(input("Please give the number to be changed into octal base:" ))
    tut.decimal_to_octal(n)

def call_base():
    """
    Call the decimal_to_basis function from import
    """
    number = int(input("Please enter a whole number tu change: "))
    basis = int(input("Please enter a whole number for the base: "))
    tut.decimal_to_basis(number, basis)

def call_chaos():
    """
    Call the chaos_turtle from import
    """
    x = int(input("Please enter a x-start point (whole number): "))
    y = int(input("Please enter a y-start poin (whole number): "))
    number = int(input("Please enter the amount of iterations (whole number): "))
    tut.chaos_turtle(x, y, number)

if __name__ == '__main__':
    menu()
