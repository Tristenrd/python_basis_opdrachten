#!/usr/bin/env python3
# Dit is de module
# In dit bestand komen alle functies.
# Je kunt de functies in een ander .py bestand gebruiken door te starten  met:
# from my_modules import csv
# my_modules/csv_mod.py

def sanitize(line):
    # kleine letters maken en spaties weghalen
    new_lst = []
    lst = line.split(',')
    for item in lst:
        new_lst.append(item.lower().strip())
    return new_lst

def create_person(lst):
    person = {
        "voornaam": lst[0],
        "tussenvoegsel": lst[1],
        "achternaam": lst[2],
        "adres": lst[3],
        "postcode": lst[4],
        "plaats": lst[5]
    }
    return person

def add_fullname(person):
    if person["tussenvoegsel"] == "":
        person['full_name'] = f"{person['voornaam'].title()} {person['achternaam'].title()}"
    else:
        person['full_name'] = f"{person['voornaam'].title()} {person['tussenvoegsel']} {person['achternaam'].title()}"
    return person

def print_persons(persons, filter=["full_name"]):
    counter = 0
    for person in persons:
        counter += 1
        for attr in filter:
            print(person[attr].title(), end=" ")
        print()
    print(f"Er zijn in totaal {counter} personen")

def do_filter(persons, veld, letter):
    result = []
    for person in persons:
        if veld in person and person[veld].lower().startswith(letter.lower()):
            result.append(person)
    return result

