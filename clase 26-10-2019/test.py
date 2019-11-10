import numpy as np
import scipy as sp

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy import spatial




def gs(X, row_vecs=True, norm = True):
    if not row_vecs:
        X = X.T
    Y = X[0:1,:].copy()
    for i in range(1, X.shape[0]):
        proj = np.diag((X[i,:].dot(Y.T)/np.linalg.norm(Y,axis=1)**2).flat).dot(Y)
        Y = np.vstack((Y, X[i,:] - proj.sum(0)))
    if norm:
        Y = np.diag(1/np.linalg.norm(Y,axis=1)).dot(Y)
    if row_vecs:
        return Y
    else:
        return Y.T




def cos(x,y):
	return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

# Projection of th evector 'y' onto the vector 'x' is the vector
def projection(x,y):
    return (np.dot(x,y)/(np.linalg.norm(x)**2))*x

def getNumberPermutations(x):
	numberPermu=0
	for enum, i in enumerate(x):
		for j in x[:enum]:
			if(i<j):
				numberPermu+=1
	return numberPermu
def adjugateMatrix(x):
	rowNum=len(x)
	colNum=len(x[0])

	m = np.linalg.det(x)
	c =[[i for i in range(colNum)] for j in range(rowNum)]
	for rowI in range(rowNum):
		for colJ in range(colNum):
			c[rowI][colJ] = (-1)*(rowI+colJ)*m
	return c

x=np.array([
		[3, 1, -1],
		[2, 0, 4],
		[5, -2, 1],
	]
)

ident=np.array([
		[1, 0, 0],
		[0, -2, 0],
		[0, 0, 1],
	]
)

# print(x*ident)

# x * ident
print(np.matmul(ident,x))

print(np.matmul(x, ident))

determ=np.array([
		[0, 0, 1, 0],
		[0, 1, 0, 0],
		[1, 0, 1, 0],
        [0, 0, 0, 1]
	]
)

print(np.linalg.det(determ))

# toInv=np.array([
# 		[1, -1, 2],
# 		[2, 1, -1],
# 		[3, 2, -2],
# 	]
# )

# print("---")
# print(np.linalg.det(toInv))
# print(np.linalg.inv(toInv))
# print(np.linalg.det(np.linalg.inv(toInv)))

toDet=np.array([
		[1, 1, -2,1],
		[2, -1, 1,-1],
		[4, 1, -3, 1],
        [1, -2, 1, 2]
	]
)


print(np.linalg.det(toDet))

