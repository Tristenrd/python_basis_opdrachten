# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete
# vragenlijst
vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# functie om gegevens op te vragen en op te slaan
def verzamel_gegevens():
    antwoorden = {}
    for index, vraag in enumerate(vragen, start=1):
        antwoord = input(f"{index}. {vraag}\n> ")
        if index == 1:
            antwoorden["voornaam"] = antwoord
        elif index == 2:
            antwoorden["achternaam"] = antwoord
        elif index == 3:
            antwoorden["drank"] = antwoord
        elif index == 4:
            antwoorden["eten"] = antwoord

    print("\nBedankt voor het invullen!")
    print("See you at the party.\n")

    # opslaan in tekstbestand
    with open("feestgangers.txt", "a") as bestand:
        bestand.write("----\n")
        for sleutel, waarde in antwoorden.items():
            bestand.write(f"{sleutel}: {waarde}\n")
        bestand.write("\n")

# programma starten
verzamel_gegevens()
