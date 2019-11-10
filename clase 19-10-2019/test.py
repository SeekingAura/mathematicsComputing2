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

# x=np.array([
# 		[1, 23, -1],
# 		[3, 43, -2],
# 		[1, -12, 1],
# 	]
# )

# print(np.linalg.det(x))
# print(np.linalg.det(adjugateMatrix(x)))

# test = np.array([[1, 1, 0], [0, 1, 1]])

x1=np.array([0,1,-1,0])
x2=np.array([2,-1,0,1])

print(np.dot(x1,x2))

# print(x1+x2)
y=np.array([1,0,1])

# print("---")
# print(x1)
# print(x2)
# print(y)
# print("---")
# xx1=projection(y, x1)

# xx2=projection(y, x2)


# print(xx1)
# print(xx2)

# print("---")

# xr=x1+x2

# print(cos(y, xr))
