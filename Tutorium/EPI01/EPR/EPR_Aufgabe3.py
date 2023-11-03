
# Aufgabe 3
# Schreiben Sie ein Python 3.x Programm, das 2 Ganzzahlen in der Konsole
# einliest, die kleinere der beiden ermittelt (wenn beide gleich
# sind, eine der beiden) und anschließend überprüft, ob diese (kleinere)
# Zahl durch 2, 4, oder 8 restlos geteilt werden kann. 
# Die entsprechenden Ergebnisse sollen dem Nutzer verständlich ausgegeben
# werden.


# Input
value_1 = int(input("Please enter a whole number: "))
value_2 = int(input("Please enter another whole number: "))

# Processing
# calculate the smaller number and store it in smaller_value_1
if value_1 <= value_2:
    smaller_value_1 = value_1
else:
    smaller_value_1 = value_2

# in form of a conditional expression
smaller_value_2 = value_1 if value_1 <= value_2 else value_2

# Definition of multiple variables in one line is possibnle
div_2, div_4, div_8 = False, False, False

if (smaller_value_1 % 8) == 0:
    div_2, div_4, div_8 = True, True, True
elif (smaller_value_1 % 4) == 0:
    div_2, div_4 = True, True
elif (smaller_value_1 % 2) == 0:
    div_2 = True

# Output
if div_2: print("Die eingegebene kleinere Zahl: ", smaller_value_1, " ist durch 2 teilbar.") 
if div_4: print("Die eingegebene kleinere Zahl: ", smaller_value_1, " ist durch 4 teilbar.")
if div_8: print("Die eingegebene kleinere Zahl: ", smaller_value_1, " ist durch 8 teilbar.")