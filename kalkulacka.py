# Jednoduchá kalkulačka v Pythonu

def secti(a, b):
    return a + b

def odecti(a, b):
    return a - b

def nasob(a, b):
    return a * b

def deleni(a, b):
    if b == 0:
        return "Chyba: dělení nulou!"
    return a / b

print("🧮 Vítej v kalkulačce")
print("Vyber operaci:")
print("1 - Sčítání")
print("2 - Odčítání")
print("3 - Násobení")
print("4 - Dělení")

volba = input("Zadej číslo operace (1/2/3/4): ")

try:
    cislo1 = float(input("Zadej první číslo: "))
    cislo2 = float(input("Zadej druhé číslo: "))

    if volba == '1':
        print("Výsledek:", secti(cislo1, cislo2))
    elif volba == '2':
        print("Výsledek:", odecti(cislo1, cislo2))
    elif volba == '3':
        print("Výsledek:", nasob(cislo1, cislo2))
    elif volba == '4':
        print("Výsledek:", deleni(cislo1, cislo2))
    else:
        print("Neplatná volba.")
except ValueError:
    print("Chyba: musíš zadat čísla.")
