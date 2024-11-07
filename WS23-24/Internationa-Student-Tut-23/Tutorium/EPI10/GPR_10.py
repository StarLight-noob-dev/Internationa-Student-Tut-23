import re
from time import sleep
# To practice and check if the created regex works
# URL = https://regex101.com/


def aufgabe_1():

    with open("Internationa-Student-Tut-23\Tutorium\EPI10\Kleopatra.txt") as k:
        words1 = [x.strip() for x in k.readlines()]
        text = "".join(i for i in words1)
        k.close()

    print(change_sie_for_er(text))


def change_sie_for_er(text:str):
    # Define a regular expression pattern for 'sie' with case-insensitive matching
    # \b<text>\b is gonna match the text ingnoring what can be before or after
    pattern = re.compile(r'\bsie\b', re.IGNORECASE)

    # Use the sub() function to replace 'sie' with 'er' in the input string
    changed_text = pattern.sub('er', text)
    return changed_text


def aufgabe_2():
    # Schreiben Sie ein kurzes Python 3.x Programm, welches mit Hilfe von regulären Ausdrücken
    # folgendes findet:

    # i. Die erste Zeichenfolge, welche mit einer Null startet, gefolgt wird von einer Zahl 
    # und anschließend einem Buchstaben. 
    # ii. Welcher alle Vorkommen aus i) findet.
    # iii. Geben Sie alle Zeichenfolgen von 2 bzw. 3 Zahlen hintereinander aus. Geben Sie 
    # ein kurzes Statement dazu ab, wie Ihre Lösung mit Fällen umgeht, die z.B. fünf 
    # Zahlen hintereinander hat „52515“ in Zeile 12.

    regex_one = '0[0-9][a-zA-Z]'
    regex_two = '[0-9]{2,3}'

    # Open the document
    with open("Internationa-Student-Tut-23\Tutorium\EPI10\Wortgitter_mitZahlen.txt") as t:
        words2 = [x.replace("\n", " ") for x in t.readlines()]
        text2 = "".join(word for word in words2) # Optionally also iterate over each String in the list
        
        # First occurence
        r1 = re.search(regex_one, text2)
        print(r1.group(0))

        # All occurence
        r2 = re.findall(regex_one, text2)
        print(r2)

        r3 = re.findall(regex_two, text2) # As i understand we use .findall that matches all non-overlaping cases
        # I manage to only take sets of 2 or 3 numbers adding the condition {} which limits the amount of 
        # characters that can be considered in the match.
        print(r3)

        t.close()
    return 

def aufgabe_3():

    reg = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    
    print("^: Asserts the start of the string.")
    sleep(1)
    print("[A-Za-z0-9._%+-]+: Matches ONE or MORE characters that are either uppercase/lowecase letters (A-Z)/(a-z), digits (0-9), or any of the following special characters: ._%+-.")
    sleep(1)
    print("@: Matches the at symbol '@'")
    sleep(1)
    print("[A-Za-z0-9.-]+: Matches ONE or MORE characters that are either uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), or the characters '.' and '-'.")
    sleep(1)
    print("\.: Escapes the dot (.) character, ensuring that it matches a literal dot. if the '\\' wasnt used it would match ANY character")
    sleep(1)
    print("[A-Za-z]{2,}: Matches two or more uppercase or lowercase letters.")
    sleep(1)
    print("$: Asserts the end of the string")
    print("Here you can see that this regex is supposed to find email addresses")

if __name__ == "__main__":
    aufgabe_1()
    aufgabe_2()
    aufgabe_3()

