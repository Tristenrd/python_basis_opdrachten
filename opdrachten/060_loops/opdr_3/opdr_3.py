# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Maak een lege lijst voor de resultaten
resultaten = []

# For-loop met range van 3 tot 81, met stappen van 3
for i in range(3, 81, 3):
    # Bereken het kwadraat van het getal en deel door 3
    resultaat = (i ** 2) / 3
    # Voeg het resultaat toe aan de lijst
    resultaten.append(resultaat)

# Toon de lijst
print(resultaten)
