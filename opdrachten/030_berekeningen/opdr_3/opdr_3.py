#Definieer de waarden van a en b
a = 4
b = -2

#Functie om de waarde van y te berekenen
def bereken_y(x):
    y = a * (x ** 3) + b * (x ** 2) - 1
    return y

#Testen met verschillende waarden van x
x = 1
print("x =", x, "De uitkomst is:", bereken_y(x))

x = 2
print("x =", x, "De uitkomst is:", bereken_y(x))

x = 0
print("x =", x, "De uitkomst is:", bereken_y(x))
