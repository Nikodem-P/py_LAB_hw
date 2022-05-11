import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

x = np.arange(1, 20, 1)
y = 1/x
# print(y)
plt.plot(x, y, ls='dotted', label="1/x")
plt.plot(x, y, 'g^')
plt.axis([1, len(x), 0, 1])
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla [1, 20]")
plt.show()
plt.savefig('wykres2.png')

x = np.arange(0, 30, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, 'r', label="sin(x)")
plt.plot(x, y2, 'b', label="cos(x)")
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
plt.savefig('wykres3.png')

iris = pd.read_csv("iris.csv", header=None, sep=',', decimal='.')
# print(iris)
irisd = {"a": iris.iloc[:, 0].values,
         "b": iris.iloc[:, 1].values,
         "c": np.random.randint(0, 50, 150)}
irisd["d"] = abs(irisd['a'] - irisd['b'])
plt.scatter('a', 'b', c='c', cmap='PiYG', s='d', data=irisd)
plt.show()
plt.savefig('wykres4,png')

xlsx = pd.ExcelFile("imiona.xlsx")
narodziny = pd.read_excel(xlsx, header=0)

grupa_plec = narodziny.groupby("Plec").agg({"Liczba" : ["sum"]})
plt.subplot(3, 1, 1)
grupa_plec.plot(kind="bar", ylabel="Urodzenia (mln)", title="Urodzenia wg płci", legend=False, rot=0)
x = narodziny["Rok"].unique()

plt.show()
