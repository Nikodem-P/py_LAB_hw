import sys as system
import math

# Zadanie 1
ulubione_sporty = ["koszykowka", "siatkowka", "plywanie"]
ulubione_sporty.reverse()
ulubione_sporty.append("bieganie")
ulubione_sporty.append("pilka nozna")

print(ulubione_sporty)
# Zadanie 2

skroty = {
    "al.": "aleja",
    "cd.": "ciag dalszy",
    "cdn.": "ciag dalszy nastapi",
    "dr": "doktor",
    "itd.": "i tak dalej",
    "itp.": "i tym podobne",
    "lek.": "lekarz",
    "mgr": "magister"
}

# Zadanie 3
ulubione_gry = {
    1: "Destiny 2",
    2: "osu!",
    3: "Overwatch",
    4: "The Elder Scrolls V: Skyrim",
    5: "Halo Infinite"
}

print("\nIlosc elementow w slowniku: %(x)d" % {'x': len(ulubione_gry)})

# Zadanie 4

napis = input("\nWprowadz zdanie: ")
liczba_a = 0

for i in napis:
    if i == "a":
        liczba_a += 1

print("Liczba liter 'a': %(x)d " % {'x': liczba_a})

# Zadanie 5

system.stdout.write("wpisz zmienne a, b, c: ")
a = int(system.stdin.readline())
b = int(system.stdin.readline())
c = int(system.stdin.readline())

wynik = a

if b != 0:
    for i in range(b-1):
        wynik *= b
else:
    wynik = 1
wynik += c

print(wynik)

# Zadanie 6

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a >= b:
    if b >= c:
        maxi = a
    else:
        if a >= c:
            maxi = a
        else:
            maxi = c
elif a < b:
    if b > c:
        maxi = b
    else:
        maxi = c

print(maxi)

# Zadanie 7

liczby = [2, 3, 4, 5, 2.2, 3.3, 4.4, 5.5]

for i in range(len(liczby)):
    liczby[i] *= liczby[i]

print(liczby)

# Zadanie 8

ilosc_liczb = 0
liczby2 = []

while ilosc_liczb < 10:
    nowa_liczba = int(input("Wprowadz liczbe numer %(x)d: " % {'x': ilosc_liczb}))
    ilosc_liczb += 1
    if nowa_liczba % 2 == 0:
        liczby2.append(nowa_liczba)

print(liczby2)

# Zadanie 9

liczba = int(input("Wprowadz liczbe: "))

try:
    print(math.sqrt(liczba))
except ValueError:
    print("Wprowadzono liczbe ujemna.")
