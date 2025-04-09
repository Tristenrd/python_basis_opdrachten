# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

#Open een bestand om de antwoorden op te slaan
bestand = "enquete_resultaten.txt"

#Stel de vragen
vraag1 = input("Wat vind je van de huidige regering? ")
vraag2 = input("Wat vind je van de Python-lessen tot nu toe? ")
vraag3 = input("Wat vind jij de mooiste stad van Nederland? ")

#Sla de antwoorden op in het bestand
with open(bestand, "a", encoding="utf-8") as f:
    f.write("Enquête Antwoorden:\n")
    f.write(f"1. Wat vind je van de huidige regering? {vraag1}\n")
    f.write(f"2. Wat vind je van de Python-lessen tot nu toe? {vraag2}\n")
    f.write(f"3. Wat vind jij de mooiste stad van Nederland? {vraag3}\n")
    f.write("-" * 40 + "\n")

print("Bedankt voor het invullen! Je antwoorden zijn opgeslagen.")