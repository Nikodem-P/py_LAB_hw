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
plt.savefig('wykres2.png')
plt.show()

x = np.arange(0, 30, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, 'r', label="sin(x)")
plt.plot(x, y2, 'b', label="cos(x)")
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig('wykres3.png')
plt.show()

iris = pd.read_csv("iris.csv", header=None, sep=',', decimal='.')
# print(iris)
irisd = {"a": iris.iloc[:, 0].values,
         "b": iris.iloc[:, 1].values,
         "c": np.random.randint(0, 50, 150)}
irisd["d"] = abs(irisd['a'] - irisd['b'])
plt.scatter('a', 'b', c='c', cmap='PiYG', s='d', data=irisd)
plt.savefig('wykres4.png')
plt.show()

xlsx = pd.ExcelFile("imiona.xlsx")
narodziny = pd.read_excel(xlsx, header=0)

grupa_plec = narodziny.groupby("Plec").agg({"Liczba": ["sum"]})
x = ['K', 'M']
y = grupa_plec.iloc[:, 0].values
plt.subplot(3, 1, 1)
plt.bar(x, y, color=['red', 'blue'])
ax = plt.gca()
ax.set_ylim([3000000, 4000000])
x = narodziny["Rok"].unique()

mezczyzni = narodziny[narodziny["Plec"] == 'M']
kobiety = narodziny[narodziny["Plec"] == 'K']
grupa_rok_m = mezczyzni.groupby("Rok").agg({"Liczba": ["sum"]})
grupa_rok_k = kobiety.groupby("Rok").agg({"Liczba": ["sum"]})
y1 = grupa_rok_m.iloc[:, 0].values
y2 = grupa_rok_k.iloc[:, 0].values
plt.subplot(3, 1, 2)
plt.plot(x, y1)
plt.plot(x, y2)
plt.xticks(range(2000, 2018, 3))
plt.subplot(3, 1, 3)
grupa_rok = narodziny.groupby("Rok").agg({"Liczba": ["sum"]})
y = grupa_rok.iloc[:, 0].values
plt.bar(x, y)
plt.axis([x[0], x[len(x)-1], 320000, 460000])
plt.tight_layout()
plt.savefig('wykres5.png')
plt.show()

