
# Exceptions are a great way to tell your user something went wrong but we dont want it to stop the 
# programm each time something happens thats why we can 'treat' them

def raise_exception(x):
    """
    Shows how the exception syntax works
    """
    # Enter a value bigger than 5
    if x < 5:
        raise ValueError("The value given has to be bigger than 5")
    print("All good have a good day")
    return

def treat_exception():
    """
    Shows how to treat an exception
    """
    while True:
        try:
            # Again imagine we ask value > 5
            x = int(input("Please enter a number: "))
            raise_exception(x)
            break
        except ValueError: #Can be used without specification but a good programmer knows what error can appear so we specify :)
            print("Something went wrong probably you gave a number smaller than 5")
    return
