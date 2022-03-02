import math
# ======
# LAB 1
# ======

# === ZAD 1 ===

a0 = "string"
a1 = "napis"
b0 = 0
b1 = 1
c0 = 0.1
c1 = 1.1
d0 = 1 + 2j
d1 = 2 + 1j

print(a0)
print(a1)
print(b0)
print(b1)
print(c0)
print(c1)
print(d0)
print(d1)

# === ZAD 2 ===

print("WARTOSC > ENTER > OPERATOR > ENTER > WARTOSC > ENTER")
wynik = 0
try:
    liczba1 = int(input())
    operator = input()
    liczba2 = int(input())
    if operator == "+":
        wynik = liczba1 + liczba2
    elif operator == "-":
        wynik = liczba1 - liczba2
    elif operator == "*":
        wynik = liczba1 * liczba2
    elif operator == "/":
        wynik = liczba1 / liczba2
    elif (operator == "**") or (operator == "^"):
        wynik = liczba1 ** liczba2
    elif (operator == "%"):
        wynik = liczba1 % liczba2
    elif (operator == "//"):
        wynik = liczba1 // liczba2
    else:
        print("Nieobslugiwany operator")

    print("Wynik: %(x)d" % {'x':wynik})
except ValueError:
    print("Niepoprawna wartosc.")
except ZeroDivisionError:
    print("Blad dzielenia przez 0.")


# === ZAD 4 ===

print(math.e ** 10)
print((math.log1p(5+(math.sin(8) ** 2)-1)**(1/6)))
print(math.floor(3.55))
print(math.ceil(4.8))

# === ZAD 5 ===

imie = "NIKODEM"
nazwisko = "PRZYBYSZEWSKI"
print(imie.capitalize() + " " + nazwisko.capitalize())

# === ZAD 6 ===

shakira = "Ven y besame mucho El mundo no importa La noche comienza No, no, no pares ahora La-la-lala, " \
          "lala-la-la-la Lala-la-lala-la-la (Porque yo siempre te llevo) (La-la-la) Lala-la, la Lala-la-la-la Lala-la, " \
          "la-la-la-la (Adentro) Leggo Leggo De to' lo que existe, llano y profundo Lo que mas quiero en este mundo " \
          "Es estar a tu lado, noche y dia Es asi como viviria"

print("la wystapilo %(x)d razy" % {"x":shakira.count("la")})

# === ZAD 7 ===

string = "Dowolna zmienna lancuchowa"
print("Druga litera to: %(x1)s, ostatnia litera to: %(x2)s" % {"x1":string[1], "x2":string[len(string)-1]})

# === ZAD 9 ===

string = "Zmienna typu string"
float = 0.1234
hex = 0x16

print("string: %(x1)s, float: %(x2)f, hex(10): %(x3)d" % {"x1":string, "x2":float, "x3":hex})
