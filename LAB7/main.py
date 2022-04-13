import numpy

# Zadanie 1

array1 = numpy.arange(4, 81, 4)
print(array1)

# Zadanie 2
array2 = numpy.arange(0.1, 5, 0.4, dtype='float64')
print(array2)
array2_int = array2.astype('int32')
print(array2_int)

# Zadanie 3

def sparr(n):
    array = numpy.empty((n, n))
    pwr = 0
    for i in range(n):
        for j in range(n):
            array[i, j] = 2 ** pwr
            pwr += 1
    return array


print(sparr(3))

# Zadanie 4

def generuj(podstawa, operacje):
    array = numpy.logspace(1, operacje, num=operacje, base=podstawa, dtype='int64')
    return array


print(generuj(3, 10))

# Zadanie 5
def vector(n):
    array = numpy.linspace(n, 1, num=n)
    matrix = numpy.diag(array, 2)
    return matrix


print(vector(5))

# Zadanie 6

words = numpy.array([list('krowa'), list('aojmi'), list('awpai'), list('aejti'), list('arjai')])
print(words)

# Zadanie 7

def slc(matrix, axis=0):
    rows, columns = matrix.shape
    if axis == 0:
        if rows % 2 == 0:
            print(matrix)
        else:
            print('blad0')
    elif axis == 1:
        if columns % 2 == 0:
            print(matrix)
            print(matrix[:, 0:(columns/2)-1])
        else:
            print('blad1')
    else:
        print('Niepoprawny parametr axis.')

slc(numpy.arange(12).reshape(3, 4), 1)
