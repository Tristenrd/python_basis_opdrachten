# Opdracht 1 functies
# Naam student:
# Groep:

def write_to_file(bestandsnaam, tekst):
    # Open het bestand in append-modus ('a'), zodat tekst wordt toegevoegd
    with open(bestandsnaam, 'a') as bestand:
        bestand.write(tekst + '\n')  # voeg een newline toe voor netheid

# Voorbeeldgebruik
my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)
