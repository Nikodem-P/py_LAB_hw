import pandas
import numpy
from matplotlib import pyplot

xlsx = pandas.ExcelFile("imiona.xlsx")
data = pandas.read_excel(xlsx, header=0)

grupa_rok = data.groupby("Rok").sum()
grupa_rok.plot(xlabel="Rok", ylabel="Liczba urodzonych", grid=True, xticks=range(2000, 2018, 1), yticks=range(360000,460000,10000))
pyplot.xticks(rotation=60)
pyplot.savefig("wykres1.png")
pyplot.show()

grupa_plec = data.groupby("Plec").agg({"Liczba" : ["sum"]})
grupa_plec.plot(kind="bar", ylabel="Urodzenia (mln)", title="Urodzenia wg płci", legend=False, rot=0)
pyplot.savefig("wykres2.png")
pyplot.show()

grupa_plec_ogr = data[data.Rok > 2012].groupby("Plec").agg({"Liczba" : ["sum"]})
grupa_plec_ogr.plot(subplots=True, kind="pie", autopct="%.0f %%", fontsize=16, legend=False, title="Urodzenia mężczyzn i kobiet w latach 2012-2017")
pyplot.savefig("wykres3.png")
pyplot.show()

data = pandas.read_csv("zamowienia.csv", header=0, sep=";", decimal=".")
zamowienia = data.groupby("Sprzedawca").count()
zamowienia["idZamowienia"].plot(kind="bar", grid=True, title="Liczba zamówień poszczególnych sprzedawców")
pyplot.xticks(rotation=30)
pyplot.grid(axis="x")
pyplot.savefig("wykres4.png")
pyplot.show()