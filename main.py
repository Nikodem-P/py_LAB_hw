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

try:
    liczba1 = int(input())
    operator = input()
    liczba2 = int(input())
    if operator == "+":
        wynik = liczba1 + liczba2
    if operator == "-":
        wynik = liczba1 - liczba2
    if operator == "*":
        wynik = liczba1 * liczba2
    if operator == "/":
        try:
            liczba1 / liczba2
        except ZeroDivisionError:
            print("Blad dzielenia przez 0.")
except ValueError:
    print("Niepoprawna wartosc.")
