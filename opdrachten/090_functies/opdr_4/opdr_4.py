# Opdracht 1 functies
# Naam student:
# Groep:

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        # Bouw de volledige naam, sla lege tussenvoegsels over zonder extra spatie
        naam = f"{persoon['voornaam']} " + (f"{persoon['tussenvoegsel']} " if persoon['tussenvoegsel'] else "") + persoon['achternaam']
        print(naam)

namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)