# Aufgabe 2
# Formel für Bonuspunkte = min(ZBNP/4, (EPR+GPR) / 14)

# Inputs
epr = int(input("Please enter the Bonus points (0-110) for EPR: ")) 
gpr = int(input("Please enter the Bonus points (0-110) for GPR: "))
zbnp = int(input("Please enter the ZBPN for the Test (normal 50): "))

# Process change
max_value = zbnp/4
bp_value = (epr + gpr) / 14

if max_value <= bp_value:
    bp_exam = max_value
else:
    bp_exam = bp_value
# Output
# F-String Interpolation and Formatting
print(f"You have {epr+gpr} bonus points. For this you are gonna recieve {bp_exam} bonus" +
        "points in the Test")
