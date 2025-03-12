my_list = []

#Maak 4 dictionaries aan met gegevens van personen
Persoon_1 = { "id": 0, "voornaam": "Michel", "achternaam": "Benard" }
Persoon_2 = { "id": 1, "voornaam": "Tristen", "achternaam": "Roeleveld" }
Persoon_3 = { "id": 2, "voornaam": "Boer", "achternaam": "Harm" }
Persoon_4 = { "id": 3, "voornaam": "Petra", "achternaam": "Patat" }

#Voeg de dictionaries toe aan de lijst
my_list.append(Persoon_1)
my_list.append(Persoon_2)
my_list.append(Persoon_3)
my_list.append(Persoon_4)

#Print de volledige naam van de 2e persoon (index 1)
print(my_list[1]["voornaam"], my_list[1]["achternaam"])