__author__ = "7727995, Calderon"

########################################### GPR ###################################################
# 1 Was ist Typisierung? Welche Art von Typisierung nutzt Python und wie unterscheidet sich
# dies von anderen Programmiersprachen?
#
# Typisierung -> Regeln zu zuordnung von Konstrukten eines Programm (var, func, Typ)
#             -> Stark und dynamish
#                   -> dynamisch: Type von variable überpruft wären programm ablaufs.
#
# 2 Worin besteht der Unterschied zwischen einer kompilierten und einer interpretierten
# Programmiersprache?
#
# Kompiler: Quellcode wird in Maschinesprache (binär) umgewandelt und führt es dann aus.
#
# Interpreter: Quell code zur Laufzeit verarbeitet wird, das heißt, dass Ziele für Ziele eine
# Anweisung eingelesen, analysier und ausgeführt bis Ende das Programm oder bis einen Fehler
# (in Quellcode) wird.
#
# 3 Byte vs Bit??
# ???
#
# 4 EVA Prinzip (CTR+C CTR+V von meine abgabe)
#Das EVA Prinzip stellt die Grundlage der Datenverarbeitung dar und besteht aus 3 Teilen:
#- Eingabe: Was soll und wie wird es gegeben (z.B Tastatur/Maus/Scanner...)
#- Verarbeitung: Wie soll die Eingabe verarbeitet
#- Ausgabe: Was wird ausgegeben und über welche Ausgabekanale (z.B Monitor/Kopfhörer/Drucker...)
#
# 5 Art von Fehler
#   TypeError:
#   IndexError:
#   SyntaxError:
#   NameError: local-global
#

########################################### EPR ############################################

# Abgabe Morgen Irgend eine Frage zu blatt 00 oder 01?

# Option 1
a, b = map(int,input("Bitte geben sie die 'a b':\t").split())

# Option 2
a = int(input("Bitte geben sie a an: "))
b = int(input("Bitte geben sie b an: "))

harmo = 2*a*b/(a+b)
arit = 0.5*(a+b)

print(f"Fas harmonische Mittel von {a} und {b} ist {harmo}")
print(f"Fas aritmetische Mittel von {a} und {b} ist {arit}")
