# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
# Vraag de gebruiker om een lijst met objecten (gescheiden door komma's)
input_data = input("Voer minimaal 5 objecten in, gescheiden door een komma:\n")

# Maak er een lijst van door de string te splitsen op komma's en spaties verwijderen
lijst = [item.strip() for item in input_data.split(",")]

# Sorteer de lijst in omgekeerde alfabetische volgorde
lijst.sort(reverse=True)

# Print de gesorteerde lijst
print(lijst)

