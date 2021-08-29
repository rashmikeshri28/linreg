from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

A = array([[1, 2], [3, 4], [5, 6]])
print('input matrix')
print(A)

M = mean(A.T, axis=1)
print('Mean')
print(M)
C = A - M
V = cov(C.T)
print('Covariance')
print(V)

values, vectors = eig(V)
print('eigen vectors')
print(vectors)
print('eigen values')
print(values)
P = vectors.T.dot(C.T)
print('reduced')
print(P.T)