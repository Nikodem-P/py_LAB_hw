import numpy

a = numpy.array([20, 30, 40, 50])
b = numpy.arange(4)
c = a + b
d = numpy.array([2.5, 65.2, 45.1, 2.6])
print(c)
print(b**3)
e = d + a
print(e)


a = numpy.arange(12).reshape((3, 4))
print(a)
print('===')
print(a.sum())
print('===')
print(a.sum(axis=0))
print('===')
print(a.sum(axis=1))
print('===')
print(a.cumsum(axis=1))
print('===')


a = numpy.arange(3)
b = numpy.arange(3)
c = a.dot(b)
print(c)
print('===')
d = numpy.array([[1,2,4], [5, 2, 4]])
e = numpy.array([[2,3], [6,3], [2, 4]])
print(e.dot(d))
print('===')


f = numpy.arange(3)
print(f)
print('===')
print(numpy.sqrt(f))
print('===')
print(numpy.cos(f))
print('===')

g = numpy.arange(6).reshape((3, 2))
print(g)

for b in g.flat:
    print(b)


print('===')

h = numpy.arange(12)
print(h)

k = h.reshape((4,3))
print(k)
print('===')
kT = k.T
print(kT)
