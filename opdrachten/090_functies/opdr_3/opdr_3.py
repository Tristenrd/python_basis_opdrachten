# Opdracht 1 functies
# Naam student:
# Groep:


import math

# Functie om het volume van een kubus te berekenen
def kubus_vol(zijde):
    return zijde ** 3

# Functie om het volume van een bol te berekenen
def bol_vol(straal):
    return (4 / 3) * math.pi * (straal ** 3)

# Voorbeeldgebruik
kubus_volume = kubus_vol(5)
print(f"De inhoud van deze kubus is: {kubus_volume}")

bol_volume = bol_vol(4)
print(f"De inhoud van deze bol is: {bol_volume}")
