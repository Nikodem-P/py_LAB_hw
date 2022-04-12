# Zadanie 1

num = []
for i in range(31):
    num.append(i)

print(num)
for i in range(31):
    num[i] *= 2

print(num)

file = open("num.txt", "w+")
file.writelines(str(num))
file.close()

# Zadanie 2

file = open("num.txt", "r")
num = file.readlines()
print(num)
file.close()

# Zadanie 3

with open("text.txt", "w+") as file:
    for i in range(1, 7):
        file.writelines("Linijka numer %(x)d\n" % {'x': i})

with open("text.txt", "r") as file:
    for line in file:
        print(line, end='')

# Zadanie 4


class NaZakupy:
    nazwa_prodkutu = ""
    ilosc = 0
    jednostka_miary = ""
    cena_jednostki = 0.0

    def __init__(self, nazwa, ilosc, jm, cena):
        self.nazwa_prodkutu = nazwa
        self.ilosc = ilosc
        self.jednostka_miary = jm
        self.cena_jednostki = cena

    def wyswietl_produkt(self):
        print(self.nazwa_prodkutu + " " + str(self.cena_jednostki) + "zl\\" + self.jednostka_miary)

    def ile_produktu(self):
        return str(self.ilosc) + self.jednostka_miary

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jednostki


ziemniak = NaZakupy("Ziemniak", 5, "kg", 3.49)
ziemniak.wyswietl_produkt()
print(ziemniak.ile_produktu())
print(ziemniak.ile_kosztuje())

# Zadanie 5


class CiagArytmetyczny:
    wartosci = []

    def wyswietl_wyrazy(self):
        print(self.wartosci)

    def pobierz_wyrazy(self):
        n = input("Ile wyrazow: ")
        for i in range(int(n)):
            a = int(input("Podaj wyraz a%(x)d: " % {'x': i + 1}))
            self.wartosci.append(a)

    def pobierz_parametry(self, a1, r, n):
        self.wartosci = [a1 + i * r for i in range(n)]

    def policz_sume(self):
        suma = 0
        for i in range(len(self.wartosci)):
            suma += self.wartosci[i]
        return suma

    # def policz_elementy
    # ???


an = CiagArytmetyczny()
an.pobierz_parametry(3, 6, 10)
an.wyswietl_wyrazy()
print(an.policz_sume())
bn = CiagArytmetyczny()
bn.pobierz_wyrazy()
bn.wyswietl_wyrazy()
print(bn.policz_sume())

# Zadanie 6


class Robaczek:
    x = 0
    y = 0
    krok = 1

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, kroki = 1):
        self.y += self.krok * kroki

    def idz_w_dol(self, kroki = 1):
        self.y -= self.krok * kroki

    def idz_w_prawo(self, kroki = 1):
        self.x += self.krok * kroki

    def idz_w_lewo(self, kroki = 1):
        self.x -= self.krok * kroki

    def gdzie_jestes(self):
        return self.x, self.y


robal = Robaczek(1, 1, 1)
robal.idz_w_lewo(2)
robal.idz_w_dol()
print(robal.gdzie_jestes())
robal.idz_w_prawo(3)
robal.idz_w_gore()
print(robal.gdzie_jestes())
