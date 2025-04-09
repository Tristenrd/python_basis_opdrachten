# Opdracht 1 modules
# Naam student:
# Groep:

# import .....
# for line in open("test.csv", 'rt'):
#   jouw code komt hier!
# main.py

from my_modules import csv_mod

persons = []

with open("test.csv", 'rt') as file:
    for line in file:
        lst = csv_mod.sanitize(line)
        person = csv_mod.create_person(lst)
        person = csv_mod.add_fullname(person)
        persons.append(person)

# Toon iedereen
print("Alle personen:")
csv_mod.print_persons(persons)

# Filter op achternaam begint met V
print("\nFilter op achternaam begint met 'V':")
filtered = csv_mod.do_filter(persons, "achternaam", "v")
csv_mod.print_persons(filtered)

# Filter op plaats begint met D
print("\nFilter op plaats begint met 'D':")
filtered = csv_mod.do_filter(persons, "plaats", "d")
csv_mod.print_persons(filtered)
