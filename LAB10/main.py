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