# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

# De rest moet jij doen.....

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)

#Variabele om het aantal pogingen bij te houden
pogingen = 0

#Start het spel
while True:
    # Vraag de gebruiker om een getal in te voeren
    poging = int(input("Raad mijn geheime getal \n"))

    # Tel het aantal pogingen
    pogingen += 1

    # Controleer of het getal correct is
    if poging < geheim_getal:
        print("Hoger")
    elif poging > geheim_getal:
        print("Lager")
    else:
        print(f"Je hebt het getal geraden, het is {geheim_getal}!")
        print(f"Je hebt het in {pogingen} keer gedaan.")
        break  # Stop de while-loop als het juiste getal is geraden
