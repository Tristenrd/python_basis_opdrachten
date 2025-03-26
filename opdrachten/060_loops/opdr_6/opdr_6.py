# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Lijst met pizza's
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
pizzas.sort()
print(pizzas)

# Voeg een nieuwe pizza toe naar eigen smaak
pizzas.append('yo-favorito')
print(pizzas)

# Verwijder de minst lekkere pizza
pizzas.remove('olivio')
print(pizzas)

# Print de eerste 3 pizza's
print(pizzas[:3])

# Print de middelste pizza
midden_index = len(pizzas) // 2
print([pizzas[midden_index]])

# Print de laatste 3 pizza's
print(pizzas[-3:])
