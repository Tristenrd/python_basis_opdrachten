# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

# Startlijst met gasten
gasten = ["Paul", "Kees", "Marie", "Hilda"]

# Voeg jezelf toe aan het begin van de lijst
gasten.insert(0, "Tristen")
print(gasten)  # Output: ["Tristen", "Paul", "Kees", "Marie", "Hilda"]

# Marie belt af -> verwijderen uit de lijst
gasten.remove("Marie")
print(gasten)  # Output: ["Tristen", "Paul", "Kees", "Hilda"]

# George wil naast Kees zitten -> toevoegen na Kees
index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")
print(gasten)  # Output: ["Tristen", "Paul", "Kees", "George", "Hilda"]
