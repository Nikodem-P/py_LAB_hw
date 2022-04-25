import numpy
import pandas

xlsx = pandas.ExcelFile("imiona.xlsx")
narodziny = pandas.read_excel(xlsx, header=0)
# print(narodziny)

# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(narodziny[narodziny["Liczba"] > 1000])

# tylko rekordy gdzie nadane imię jest takie jak Twoje
print(narodziny[narodziny["Imie"] == "NIKODEM"])

# sumę wszystkich urodzonych dzieci w całym danym okresie
# narodziny_lata = narodziny.groupby(["Rok"])
print(narodziny.agg({"Liczba" : ["sum"]}))

# sumę dzieci urodzonych w latach 2000-2005
narodziny_lata_ograniczone = narodziny[narodziny["Rok"] <= 2005].groupby(["Rok"])
print(narodziny_lata_ograniczone.agg({"Liczba" : ["sum"]}))

# sumę urodzonych chłopców i dziewczynek
narodziny_plec = narodziny.groupby(["Plec"])
print(narodziny_plec.agg({"Liczba" : ["sum"]}))

# najbardziej popularne imię dziewczynki i chłopca w danym roku (czyli po 2 rekordy na rok)
# print(narodziny.groupby(["Rok"]).agg({"Liczba" : ["max"]}))
