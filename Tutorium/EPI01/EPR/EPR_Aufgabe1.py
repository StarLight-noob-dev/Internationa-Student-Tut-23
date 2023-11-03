########################################## EPR #########################################

# Aufgabe 1
# a)
a = 11.0
if a > 5:
    print("Größer als 5")
elif a > 10:
    print("Größer als 10")

# run:    Ja
# output: Größer als 5
# reason: da 'if' schon behandelt, geht er nicht in elif!


# b)
a = 4,2
if a > 4:
    print("Die Zahl ist zu groß.")
else:
    print("Gültige Eingabe.")

# What data type is a?
# run:      Nein
# output:   Error Message TypeError
# reason:   a is not an int is a Tuple which doesnt have '>' operator


# c
a = 2
a = b
a == 8
if a == b:
    print("Sind gleich: ", a)

# run:      Nein 
# output:   Error NameError: 'b' is not defined
# reason:


a = 5
b = 10
if b:
    print("b gibt True")
else: print("b gibt False")

# run:   Ja
# output:   b gibt True
# reason:   any number other than 0 returns true
