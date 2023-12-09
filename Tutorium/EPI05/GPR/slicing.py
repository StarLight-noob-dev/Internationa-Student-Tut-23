
def slicing():
    """
    Shows the soution for the slicing
    """

    s = "Ich mag programmieren"

    while True:
        c = input("Which aufgabe do u want to see? (a-g) or exit ")

        match c:
            case "a":
                print(f"Solution to Aufgabe a is: {s[::-2]}\n")
            case "b":
                print(f"Solution to Aufgabe b is: {s[4:8]}\n")
            case "c":
                print(f"Solution to Aufgabe c is: {s[:8]}\n")
            case "d":
                print(f"Solution to Aufgabe d is: {s[1:]}\n")
            case "e":
                print(f"Solution to Aufgabe e is: {s[:3:-1]}\n")
            case "f":
                print(f"Solution to Aufgabe f is: {s[-2:-9:-2]}\n")
            case "exit":
                break
            case _:
                print("This option is not available\n")

def find_in_string(text, word):

    for i in range(len(text)):
        if text[i:i+len(word)] == word:
            print(i)
            return
        
    print("Word wasnt found in the text")


#slicing()
#find_in_string("Hello World", "World")