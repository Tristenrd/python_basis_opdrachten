# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ...

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

# Hier de rest van jouw code...
# Lijst van beschikbare toppings en hun prijzen
toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]

# Maak een lijst met alleen de namen van de toppings
beschikbare_toppings = [topping[0] for topping in toppings]

# Vraag de gebruiker om een topping te kiezen
keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n")

# Controleer of de keuze geldig is
geknopte_topping = next((topping for topping in toppings if topping[0].lower() == keuze.lower()), None)

if geknopte_topping:
    # Als de keuze geldig is, print de topping en de prijs
    print(f"U heeft {geknopte_topping[0]} besteld. Dat kost {geknopte_topping[1]}")
else:
    # Als de keuze niet geldig is, print een foutmelding
    print("Uw keuze zit niet in ons assortiment")
