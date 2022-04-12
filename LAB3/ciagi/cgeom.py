def generuj(n, q, a1 = 1):
    wyrazy = [(a1 * (q ** i)) for i in range(n)]
    return wyrazy

def suma(wyrazy):
    suma = 0
    for i in wyrazy:
        suma += i
    return suma

def monotonicznosc(wyrazy):
    if wyrazy[1] / wyrazy[0] > 1:
        return 1
    elif wyrazy[1] - wyrazy[0] == 1:
        return 0
    elif wyrazy[1] / wyrazy[0] < 1 and wyrazy[1] / wyrazy[0] > 0:
        return -1
    else:
        return None