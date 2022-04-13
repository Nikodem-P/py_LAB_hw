import numpy

# Zadanie 1
matrix1 = numpy.arange(3)
matrix2 = numpy.arange(3)
print(matrix1 * matrix2)
print('===============')

# Zadanie 2
matrix3 = numpy.arange(9).reshape(3, 3)
print(matrix3)
print('Wartosci maksymalne w kolumnach:')
print(matrix3.min(axis=0))
print('Wartosci maksymalne w wierszach:')
print(matrix3.min(axis=1))
print('Wartosci minimalne w kolumnach:')
print(matrix3.max(axis=0))
print('Wartosci minimalne w wierszach:')
print(matrix3.max(axis=1))
print('===============')

# Zadanie 3
print(matrix1.dot(matrix2))
print('===============')

# Zadanie 4
matrix4 = numpy.arange(3, dtype='int64')
matrix5 = numpy.array([[4.6, 7.9, 2.3]])
print(matrix4 * matrix5)
print('===============')

# Zadanie 5
matrix6 = numpy.arange(6).reshape(2, 3)
a = numpy.sin(matrix6)
print(a)
print('===============')

# Zadanie 6
matrix7 = numpy.arange(10, 22, 2).reshape(2, 3)
b = numpy.cos(matrix7)
print(b)
print('===============')

# Zadanie 7
print(a + b)
print('===============')

# Zadanie 8
matrix8 = numpy.arange(9).reshape(3,3)
for i in matrix8:
    print(i)
print('===============')

# Zadanie 9
matrix10 = numpy.arange(9).reshape(3,3)
for i in matrix8.flat:
    print(i)
print('===============')

# Zadanie 10
matrix9 = numpy.arange(81).reshape(9, 9)
print(matrix9)
matrix9a = matrix9.reshape(1,81)
print(matrix9a)
matrix9b = matrix9.reshape(81,1)
print(matrix9b)
matrix9c = matrix9.reshape(3,27)
print(matrix9c)
matrix9d = matrix9.reshape(27,3)
print(matrix9d)
# Wszystkie dzieliniki liczby 81

# Zadanie 11
matrix11 = numpy.arange(12).reshape(3, 4)
matrix12 = numpy.arange(12).reshape(4, 3)
matrix13 = numpy.arange(12).reshape(2, 6)

print(matrix11.flatten())
print(matrix12.flatten())
print(matrix13.flatten())

# Tak.
