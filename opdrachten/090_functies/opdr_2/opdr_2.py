# Opdracht 1 functies
# Naam student:
# Groep:

# Functie om kilometers naar miles om te rekenen
def kilometers_naar_miles(km):
    return km / 1.609344

# Functie om miles naar kilometers om te rekenen
def miles_naar_kilometers(miles):
    return miles * 1.609344

# Voorbeeldgebruik
kilometers = 1223
miles = 867

# Berekeningen uitvoeren
miles_resultaat = kilometers_naar_miles(kilometers)
kilometers_resultaat = miles_naar_kilometers(miles)

# Output op het scherm
print(f"{kilometers} kilometers = {miles_resultaat} miles")
print(f"{miles} miles = {kilometers_resultaat} kilometers")
