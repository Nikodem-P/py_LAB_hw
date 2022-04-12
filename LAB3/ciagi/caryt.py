def generuj(n, r, a1 = 0):
    wyrazy = [(a1 + i * r) for i in range(n)]
    return wyrazy

def suma(wyrazy):
    suma = 0
    for i in wyrazy:
        suma += i
    return suma

def monotonicznosc(wyrazy):
    if wyrazy[1] - wyrazy[0] > 0:
        return 1
    elif wyrazy[1] - wyrazy[0] == 0:
        return 0
    else:
        return -1