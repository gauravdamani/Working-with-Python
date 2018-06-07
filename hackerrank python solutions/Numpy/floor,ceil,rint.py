import numpy

A = numpy.array(list(map(float, input().split())), float)
numpy.set_printoptions(sign=' ')
print (numpy.floor(A))
print (numpy.ceil(A))
print (numpy.rint(A))