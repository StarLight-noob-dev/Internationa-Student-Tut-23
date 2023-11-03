# Aufgabe 2
# Formel für Bonuspunkte = min(ZBNP/4, (EPR+GPR) / 14)

# Inputs
epr = int(input("Please enter the Bonus points (0-110) for EPR: ")) 
gpr = int(input("Please enter the Bonus points (0-110) for GPR: "))
zbnp = int(input("Please enter the ZBPN for the Test (normal 50): "))

# Process change
klausur_points = 1

# Output
# F-String Interpolation and Formatting
print(f"You have {epr+gpr} bonus points. For this you are gonna recieve {klausur_points} bonus" +
        "points in the Test")
