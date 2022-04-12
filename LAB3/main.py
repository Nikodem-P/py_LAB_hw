import random

# Zadanie 1

# A = []
# for x in range(1,11):
#     A.append(1-x)
# print(A)

A = [1-x for x in range(1, 11)]
print(A)

# B = []
# for x in range (8):
#     B.append(4**x)
# print(B)

B = [4**x for x in range(8)]
print(B)

# C = []
# for x in B:
#     if x % 2 == 0:
#         C.append(x)
# print(C)

C = [x for x in B if x % 2 == 0]
print(C)

# Zadanie 2

lista = []
for i in range(10):
    lista.append(random.randint(0, 100))

nowa_lista = [x for x in lista if x % 2 == 0]

print(lista)
print(nowa_lista)

# Zadanie 3
# ???

# Zadanie 4

def czy_trojkat_prostokatny(a, b, c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        return 1
    else:
        return 0

print(czy_trojkat_prostokatny(5,5,4))

# Zadanie 5

def pole_trapezu(a = 1, b = 1, h = 1):
    return ((a + b) * h) / 2

print(pole_trapezu(1,3))

# Zadanie 6

def iloczyn_ciagu(a = 1, b = 4, ile = 10):
    wynik = a
    for i in range(1, ile + 1):
        print("{}".format(wynik) + " * {}".format(b))
        wynik *= b
    return wynik

print(iloczyn_ciagu())
print(iloczyn_ciagu(3,8,3))

# Zadanie 7

def iloczyn_gwiazdka(*wyrazy_ciagu):
    wynik = 1
    for i in wyrazy_ciagu:
        wynik *= i
    return wynik

print(iloczyn_gwiazdka(1, 2, 2, 2, 3))

# Zadanie 8

def lista_zakupow(**produkt):
    ilosc = 0
    suma = 0
    for key, value in produkt.items():
        ilosc += 1
        suma += value
    return ilosc, suma

produkty = {
        "mleko": 3.50,
        "czekolada": 4.90,
        "chleb": 2.90
}

print(lista_zakupow(**produkty))

# Zadanie 9

from ciagi import *
an = caryt.generuj(13,-6)
print(an)
print(caryt.suma(an))
print(caryt.monotonicznosc(an))

bn = cgeom.generuj(10, 0.5, 2)
print(bn)
print(cgeom.suma(bn))
print(cgeom.monotonicznosc(bn))
