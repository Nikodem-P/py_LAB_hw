import numpy
import pandas

xlsx = pandas.ExcelFile("imiona.xlsx")
narodziny = pandas.read_excel(xlsx, header=0)
# print(narodziny)

print(narodziny[narodziny["Liczba"] > 1000])

print(narodziny[narodziny["Imie"] == "NIKODEM"])

narodziny_lata = narodziny.groupby(["Rok"])
print(narodziny_lata.agg({"Rok" : ["sum"]}))
print(narodziny_lata.agg({"Rok" : ["sum"]}))

narodziny_lata_ograniczone = narodziny[narodziny["Rok"] <= 2005].groupby(["Rok"])
print(narodziny_lata_ograniczone.agg({"Rok" : ["sum"]}))

