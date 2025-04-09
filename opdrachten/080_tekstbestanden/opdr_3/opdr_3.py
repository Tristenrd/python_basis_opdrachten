# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:
def encrypt(zin, sleutel):
    versleuteld = ""

    for letter in zin:
        if letter.isalpha():  # Controleer of het een letter is
            start = ord('A') if letter.isupper() else ord('a')
            nieuwe_letter = chr(start + (ord(letter) - start + sleutel) % 26)
        else:
            nieuwe_letter = letter  # Laat leestekens en spaties hetzelfde

        versleuteld += nieuwe_letter

    return versleuteld


#Vraag de gebruiker om invoer
zin = input("Geef de tekst die je wilt encrypten:\n")
sleutel = 5  # Aantal stappen om te verschuiven

#Voer de encryptie uit en print het resultaat
versleutelde_zin = encrypt(zin, sleutel)
print("\nVersleuteld:")
print(versleutelde_zin)


